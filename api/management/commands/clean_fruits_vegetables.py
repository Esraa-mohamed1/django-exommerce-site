from django.core.management.base import BaseCommand
from api.models import Category, Product

class Command(BaseCommand):
    help = 'Delete all products and categories related to fruits and vegetables'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be deleted without actually deleting',
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        
        if dry_run:
            self.stdout.write(self.style.WARNING('DRY RUN MODE - No changes will be made'))
        
        # Keywords to identify fruits and vegetables
        fruit_veg_keywords = [
            'fruit', 'fruits', 'vegetable', 'vegetables', 'apple', 'banana', 'orange',
            'grape', 'strawberry', 'blueberry', 'raspberry', 'blackberry', 'cherry',
            'peach', 'pear', 'plum', 'apricot', 'mango', 'pineapple', 'kiwi', 'lemon',
            'lime', 'grapefruit', 'watermelon', 'cantaloupe', 'honeydew', 'carrot',
            'broccoli', 'cauliflower', 'spinach', 'lettuce', 'tomato', 'potato',
            'onion', 'garlic', 'pepper', 'cucumber', 'zucchini', 'eggplant', 'corn',
            'peas', 'beans', 'celery', 'asparagus', 'mushroom', 'avocado', 'olive'
        ]
        
        # Find categories that might be related to fruits/vegetables
        fruit_veg_categories = []
        for category in Category.objects.all():
            category_name_lower = category.name.lower()
            if any(keyword in category_name_lower for keyword in fruit_veg_keywords):
                fruit_veg_categories.append(category)
        
        # Find products that might be related to fruits/vegetables
        fruit_veg_products = []
        for product in Product.objects.all():
            product_name_lower = product.name.lower()
            product_desc_lower = product.description.lower()
            
            # Check if product name or description contains fruit/veg keywords
            if any(keyword in product_name_lower or keyword in product_desc_lower 
                   for keyword in fruit_veg_keywords):
                fruit_veg_products.append(product)
        
        # Display what will be deleted
        self.stdout.write('=== FRUITS AND VEGETABLES CLEANUP ===')
        
        if fruit_veg_categories:
            self.stdout.write('\n📁 Categories to be deleted:')
            for category in fruit_veg_categories:
                self.stdout.write(f'   - {category.name} (ID: {category.id})')
        else:
            self.stdout.write('\n✅ No fruit/vegetable categories found')
        
        if fruit_veg_products:
            self.stdout.write('\n🍎 Products to be deleted:')
            for product in fruit_veg_products:
                self.stdout.write(f'   - {product.name} (ID: {product.id}) - ${product.price}')
        else:
            self.stdout.write('\n✅ No fruit/vegetable products found')
        
        if not fruit_veg_categories and not fruit_veg_products:
            self.stdout.write(self.style.SUCCESS('\n🎉 No fruits or vegetables found in the database!'))
            return
        
        # Perform deletion if not dry run
        if not dry_run:
            deleted_products = 0
            deleted_categories = 0
            
            # Delete products first (to avoid foreign key issues)
            for product in fruit_veg_products:
                product_name = product.name
                product.delete()
                deleted_products += 1
                self.stdout.write(f'🗑️  Deleted product: {product_name}')
            
            # Delete categories
            for category in fruit_veg_categories:
                category_name = category.name
                category.delete()
                deleted_categories += 1
                self.stdout.write(f'🗑️  Deleted category: {category_name}')
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'\n✅ Cleanup completed! Deleted {deleted_products} products and {deleted_categories} categories.'
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    f'\n⚠️  DRY RUN: Would delete {len(fruit_veg_products)} products and {len(fruit_veg_categories)} categories.'
                )
            )
            self.stdout.write('Run without --dry-run to actually perform the deletion.') 