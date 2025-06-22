from django.core.management.base import BaseCommand
from api.models import Category, Product

class Command(BaseCommand):
    help = 'Populate the database with candy products for Marsemell'

    def handle(self, *args, **options):
        self.stdout.write('Creating candy categories...')
        
        # Create candy categories
        categories_data = [
            {
                'name': 'Chocolates',
                'description': 'Delicious chocolate candies and treats'
            },
            {
                'name': 'Gummies',
                'description': 'Chewy and fruity gummy candies'
            },
            {
                'name': 'Hard Candies',
                'description': 'Classic hard candies and lollipops'
            },
            {
                'name': 'Jelly Beans',
                'description': 'Colorful and flavorful jelly beans'
            },
            {
                'name': 'Caramels',
                'description': 'Soft and chewy caramel candies'
            }
        ]
        
        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')
        
        self.stdout.write('Creating candy products...')
        
        # Candy products with new image URLs
        products_data = [
            {
                'name': 'Pink Heart Chocolates',
                'description': 'Delicious pink chocolate hearts perfect for sharing love',
                'price': 12.99,
                'stock': 50,
                'image': 'https://th.bing.com/th/id/OIP.e4s69NeggNhPuvnUKgmEWgAAAA?w=194&h=194&c=7&r=0&o=7&pid=1.7&rm=3',
                'category': 'Chocolates'
            },
            {
                'name': 'Rainbow Gummy Bears',
                'description': 'Colorful and fruity gummy bears in all your favorite flavors',
                'price': 8.99,
                'stock': 75,
                'image': 'https://ts4.mm.bing.net/th?id=OIP.lE-YnK9FlLsOP1iAxksdLgHaE8&pid=15.1',
                'category': 'Gummies'
            },
            {
                'name': 'Pink Cotton Candy',
                'description': 'Fluffy pink cotton candy that melts in your mouth',
                'price': 6.99,
                'stock': 30,
                'image': 'https://th.bing.com/th/id/OIP.qXI7vd56LL3jFuppQzyPBQHaMy?r=0&pid=ImgDet&w=190&h=329&c=7&cb=idpwebpc2',
                'category': 'Hard Candies'
            },
            {
                'name': 'Strawberry Lollipops',
                'description': 'Sweet strawberry flavored lollipops with pink swirls',
                'price': 4.99,
                'stock': 100,
                'image': 'https://ts3.mm.bing.net/th?id=OIP.a7PY1kmxaAWFUR7AjNBpLQHaES&pid=15.1',
                'category': 'Hard Candies'
            },
            {
                'name': 'Pink Jelly Beans',
                'description': 'Assorted pink jelly beans with various fruity flavors',
                'price': 7.99,
                'stock': 60,
                'image': 'https://ts2.mm.bing.net/th?id=OIP.IcYLreAmfIPL7uvJKNI5QgHaHa&pid=15.1',
                'category': 'Jelly Beans'
            },
            {
                'name': 'Rose Petal Chocolates',
                'description': 'Elegant chocolates with rose petal decoration',
                'price': 15.99,
                'stock': 25,
                'image': 'https://th.bing.com/th/id/OIP.e4s69NeggNhPuvnUKgmEWgAAAA?w=194&h=194&c=7&r=0&o=7&pid=1.7&rm=3',
                'category': 'Chocolates'
            },
            {
                'name': 'Pink Marshmallows',
                'description': 'Soft and fluffy pink marshmallows',
                'price': 5.99,
                'stock': 80,
                'image': 'https://ts4.mm.bing.net/th?id=OIP.lE-YnK9FlLsOP1iAxksdLgHaE8&pid=15.1',
                'category': 'Gummies'
            },
            {
                'name': 'Cherry Caramels',
                'description': 'Sweet cherry flavored caramels wrapped in pink foil',
                'price': 9.99,
                'stock': 45,
                'image': 'https://th.bing.com/th/id/OIP.qXI7vd56LL3jFuppQzyPBQHaMy?r=0&pid=ImgDet&w=190&h=329&c=7&cb=idpwebpc2',
                'category': 'Caramels'
            },
            {
                'name': 'Pink Rock Candy',
                'description': 'Beautiful pink rock candy crystals on sticks',
                'price': 11.99,
                'stock': 35,
                'image': 'https://ts3.mm.bing.net/th?id=OIP.a7PY1kmxaAWFUR7AjNBpLQHaES&pid=15.1',
                'category': 'Hard Candies'
            },
            {
                'name': 'Strawberry Gummy Worms',
                'description': 'Long and chewy strawberry gummy worms',
                'price': 6.99,
                'stock': 70,
                'image': 'https://ts2.mm.bing.net/th?id=OIP.IcYLreAmfIPL7uvJKNI5QgHaHa&pid=15.1',
                'category': 'Gummies'
            },
            {
                'name': 'Pink Chocolate Truffles',
                'description': 'Luxurious pink chocolate truffles with smooth centers',
                'price': 18.99,
                'stock': 20,
                'image': 'https://th.bing.com/th/id/OIP.e4s69NeggNhPuvnUKgmEWgAAAA?w=194&h=194&c=7&r=0&o=7&pid=1.7&rm=3',
                'category': 'Chocolates'
            },
            {
                'name': 'Rose Water Jelly Beans',
                'description': 'Elegant rose water flavored jelly beans',
                'price': 12.99,
                'stock': 40,
                'image': 'https://ts4.mm.bing.net/th?id=OIP.lE-YnK9FlLsOP1iAxksdLgHaE8&pid=15.1',
                'category': 'Jelly Beans'
            }
        ]
        
        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'stock': product_data['stock'],
                    'image': product_data['image'],
                    'category': categories[product_data['category']]
                }
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated Marsemell with candy products!')
        ) 