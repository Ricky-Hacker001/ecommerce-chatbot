from app import app
from extensions import db
from models import Product, User

with app.app_context():
    db.drop_all()
    db.create_all()

    # Realistic product data
    products_data = [
        {
            "name": "iPhone 14 Pro",
            "category": "Smartphone",
            "brand": "Apple",
            "price": 99999.99,
            "description": "Latest Apple iPhone with A16 Bionic chip and ProMotion display.",
            "image_url": "https://example.com/images/iphone14pro.jpg"
        },
        {
            "name": "Samsung Galaxy S23 Ultra",
            "category": "Smartphone",
            "brand": "Samsung",
            "price": 89999.00,
            "description": "Samsung's flagship smartphone with 200MP camera and S-Pen.",
            "image_url": "https://example.com/images/galaxys23ultra.jpg"
        },
        {
            "name": "Sony WH-1000XM5",
            "category": "Headphones",
            "brand": "Sony",
            "price": 29999.50,
            "description": "Industry-leading noise canceling wireless headphones.",
            "image_url": "https://example.com/images/sonywh1000xm5.jpg"
        },
        {
            "name": "Canon EOS R6",
            "category": "Camera",
            "brand": "Canon",
            "price": 159999.99,
            "description": "Full-frame mirrorless camera with outstanding autofocus.",
            "image_url": "https://example.com/images/canoneosr6.jpg"
        },
        {
            "name": "Lenovo ThinkPad X1 Carbon",
            "category": "Laptop",
            "brand": "Lenovo",
            "price": 129999.00,
            "description": "Lightweight business laptop with robust performance.",
            "image_url": "https://example.com/images/thinkpadx1carbon.jpg"
        },
        {
            "name": "Apple MacBook Air M2",
            "category": "Laptop",
            "brand": "Apple",
            "price": 119999.99,
            "description": "Thin and powerful laptop with Apple's M2 chip.",
            "image_url": "https://example.com/images/macbookairm2.jpg"
        },
        {
            "name": "Samsung Galaxy Tab S8",
            "category": "Tablet",
            "brand": "Samsung",
            "price": 59999.00,
            "description": "High-performance Android tablet with S-Pen support.",
            "image_url": "https://example.com/images/galaxytabs8.jpg"
        },
        {
            "name": "Apple iPad Pro 12.9",
            "category": "Tablet",
            "brand": "Apple",
            "price": 109999.99,
            "description": "Powerful iPad with Liquid Retina XDR display.",
            "image_url": "https://example.com/images/ipadpro12.jpg"
        },
        {
            "name": "Sony Alpha a7 III",
            "category": "Camera",
            "brand": "Sony",
            "price": 139999.00,
            "description": "Full-frame mirrorless camera with 4K video.",
            "image_url": "https://example.com/images/sonya7iii.jpg"
        },
        {
            "name": "Bose QuietComfort Earbuds",
            "category": "Headphones",
            "brand": "Bose",
            "price": 24999.00,
            "description": "True wireless earbuds with noise cancellation.",
            "image_url": "https://example.com/images/boseqcbuds.jpg"
        },
        {
            "name": "Dell XPS 13",
            "category": "Laptop",
            "brand": "Dell",
            "price": 99999.00,
            "description": "Compact and powerful ultrabook with InfinityEdge display.",
            "image_url": "https://example.com/images/dellxps13.jpg"
        },
        {
            "name": "Google Pixel 7",
            "category": "Smartphone",
            "brand": "Google",
            "price": 64999.00,
            "description": "Google’s flagship smartphone with excellent camera software.",
            "image_url": "https://example.com/images/pixel7.jpg"
        },
        {
            "name": "JBL Charge 5",
            "category": "Headphones",
            "brand": "JBL",
            "price": 14999.00,
            "description": "Portable Bluetooth speaker with powerful sound.",
            "image_url": "https://example.com/images/jblcharge5.jpg"
        },
        {
            "name": "Microsoft Surface Pro 9",
            "category": "Tablet",
            "brand": "Microsoft",
            "price": 89999.00,
            "description": "Versatile 2-in-1 device with touchscreen and keyboard.",
            "image_url": "https://example.com/images/surfacepro9.jpg"
        },
        {
            "name": "Canon EOS M50 Mark II",
            "category": "Camera",
            "brand": "Canon",
            "price": 54999.00,
            "description": "Compact mirrorless camera with excellent video features.",
            "image_url": "https://example.com/images/canoneosm50ii.jpg"
        },
        {
            "name": "Apple AirPods Pro 2",
            "category": "Headphones",
            "brand": "Apple",
            "price": 24999.00,
            "description": "Wireless earbuds with active noise cancellation and transparency mode.",
            "image_url": "https://example.com/images/airpodspro2.jpg"
        },
        {
            "name": "Asus ROG Zephyrus G14",
            "category": "Laptop",
            "brand": "Asus",
            "price": 139999.99,
            "description": "Gaming laptop with powerful AMD Ryzen processor.",
            "image_url": "https://example.com/images/rogzephyrusg14.jpg"
        },
        {
            "name": "Samsung Galaxy Buds Pro",
            "category": "Headphones",
            "brand": "Samsung",
            "price": 17999.00,
            "description": "True wireless earbuds with intelligent ANC.",
            "image_url": "https://example.com/images/galaxybudspro.jpg"
        },
        {
            "name": "Lenovo Yoga 9i",
            "category": "Laptop",
            "brand": "Lenovo",
            "price": 124999.00,
            "description": "Convertible 2-in-1 laptop with premium build quality.",
            "image_url": "https://example.com/images/lenovoyoga9i.jpg"
        },
        {
            "name": "Google Nest Hub",
            "category": "Tablet",
            "brand": "Google",
            "price": 7999.00,
            "description": "Smart display with Google Assistant built-in.",
            "image_url": "https://example.com/images/nesthub.jpg"
        },
        {
        "name": "OnePlus 11",
        "category": "Smartphone",
        "brand": "OnePlus",
        "price": 49999.99,
        "description": "Flagship killer with Snapdragon 8 Gen 2 processor.",
        "image_url": "https://example.com/images/oneplus11.jpg"
        },
        {
            "name": "HP Spectre x360",
            "category": "Laptop",
            "brand": "HP",
            "price": 114999.00,
            "description": "Convertible laptop with sleek design and strong performance.",
            "image_url": "https://example.com/images/hpspectrex360.jpg"
        },
        {
            "name": "Amazon Echo Show 8",
            "category": "Tablet",
            "brand": "Amazon",
            "price": 9999.00,
            "description": "Smart display with Alexa and 8-inch HD screen.",
            "image_url": "https://example.com/images/echoshow8.jpg"
        },
        {
            "name": "DJI Mini 3 Pro",
            "category": "Camera",
            "brand": "DJI",
            "price": 75999.00,
            "description": "Compact drone with advanced camera capabilities.",
            "image_url": "https://example.com/images/djimini3pro.jpg"
        },
        {
            "name": "Beats Studio3 Wireless",
            "category": "Headphones",
            "brand": "Beats",
            "price": 21999.00,
            "description": "Over-ear wireless headphones with active noise canceling.",
            "image_url": "https://example.com/images/beatsstudio3.jpg"
        },
        {
            "name": "Google Pixelbook Go",
            "category": "Laptop",
            "brand": "Google",
            "price": 84999.00,
            "description": "Lightweight Chromebook with long battery life.",
            "image_url": "https://example.com/images/pixelbookgo.jpg"
        },
        {
            "name": "Fujifilm X-T4",
            "category": "Camera",
            "brand": "Fujifilm",
            "price": 139999.00,
            "description": "Mirrorless camera with in-body stabilization and excellent color science.",
            "image_url": "https://example.com/images/fujifilmxt4.jpg"
        },
        {
            "name": "Microsoft Surface Laptop 5",
            "category": "Laptop",
            "brand": "Microsoft",
            "price": 109999.00,
            "description": "Premium laptop with touchscreen and slim design.",
            "image_url": "https://example.com/images/surfacelaptop5.jpg"
        },
        {
            "name": "Jabra Elite 85t",
            "category": "Headphones",
            "brand": "Jabra",
            "price": 17999.00,
            "description": "True wireless earbuds with adjustable ANC and great call quality.",
            "image_url": "https://example.com/images/jabraelite85t.jpg"
        },
        {
            "name": "Lenovo Legion 5",
            "category": "Laptop",
            "brand": "Lenovo",
            "price": 124999.00,
            "description": "Gaming laptop with AMD Ryzen 7 and NVIDIA RTX graphics.",
            "image_url": "https://example.com/images/legion5.jpg"
        },
        {
            "name": "Samsung Galaxy Watch 5",
            "category": "Smartwatch",
            "brand": "Samsung",
            "price": 24999.00,
            "description": "Advanced smartwatch with health tracking and LTE.",
            "image_url": "https://example.com/images/galaxywatch5.jpg"
        },
        {
            "name": "Apple Watch Series 8",
            "category": "Smartwatch",
            "brand": "Apple",
            "price": 39999.00,
            "description": "Latest Apple smartwatch with ECG and temperature sensor.",
            "image_url": "https://example.com/images/applewatch8.jpg"
        },
        {
            "name": "Anker Soundcore Liberty Air 2",
            "category": "Headphones",
            "brand": "Anker",
            "price": 7999.00,
            "description": "Affordable true wireless earbuds with great sound quality.",
            "image_url": "https://example.com/images/soundcorelibertyair2.jpg"
        },
        {
            "name": "GoPro Hero 11 Black",
            "category": "Camera",
            "brand": "GoPro",
            "price": 49999.00,
            "description": "Action camera with HyperSmooth 5.0 stabilization and 5.3K video.",
            "image_url": "https://example.com/images/goprohero11.jpg"
        },
        {
            "name": "Razer Blade 15",
            "category": "Laptop",
            "brand": "Razer",
            "price": 189999.00,
            "description": "High-end gaming laptop with powerful GPU and sleek design.",
            "image_url": "https://example.com/images/razerblade15.jpg"
        },
        {
            "name": "Sony WF-1000XM4",
            "category": "Headphones",
            "brand": "Sony",
            "price": 19999.00,
            "description": "Premium true wireless earbuds with industry-leading noise cancellation.",
            "image_url": "https://example.com/images/sonywf1000xm4.jpg"
        },
        {
            "name": "Samsung Galaxy Z Fold 5",
            "category": "Smartphone",
            "brand": "Samsung",
            "price": 179999.00,
            "description": "Foldable smartphone with large dynamic AMOLED display.",
            "image_url": "https://example.com/images/galaxyzfold5.jpg"
        },
        {
            "name": "Lenovo Tab P12 Pro",
            "category": "Tablet",
            "brand": "Lenovo",
            "price": 54999.00,
            "description": "High-end Android tablet with AMOLED display and pen support.",
            "image_url": "https://example.com/images/lenovotabp12pro.jpg"
        },
        {
            "name": "Apple iMac 24-inch M1",
            "category": "Desktop",
            "brand": "Apple",
            "price": 139999.99,
            "description": "All-in-one desktop with Apple M1 chip and vibrant Retina display.",
            "image_url": "https://example.com/images/imac24m1.jpg"
        },
        {
            "name": "Dell UltraSharp U2723QE",
            "category": "Monitor",
            "brand": "Dell",
            "price": 44999.00,
            "description": "27-inch 4K UHD monitor with excellent color accuracy.",
            "image_url": "https://example.com/images/dellultrasharpu2723qe.jpg"
        },
         {
        "name": "ASUS ROG Strix G15",
        "category": "Laptop",
        "brand": "ASUS",
        "price": 134999.00,
        "description": "Powerful gaming laptop with AMD Ryzen 9 and NVIDIA RTX 3070.",
        "image_url": "https://example.com/images/asusrogstrixg15.jpg"
        },
        {
            "name": "Sony Alpha a7 IV",
            "category": "Camera",
            "brand": "Sony",
            "price": 219999.00,
            "description": "Full-frame mirrorless camera with 33MP sensor and 4K video.",
            "image_url": "https://example.com/images/sonya7iv.jpg"
        },
        {
            "name": "Bose QuietComfort 45",
            "category": "Headphones",
            "brand": "Bose",
            "price": 24999.00,
            "description": "Industry-leading noise-cancelling headphones with high comfort.",
            "image_url": "https://example.com/images/boseqc45.jpg"
        },
        {
            "name": "Apple iPad Air (5th Gen)",
            "category": "Tablet",
            "brand": "Apple",
            "price": 54999.00,
            "description": "Powerful tablet with M1 chip and Liquid Retina display.",
            "image_url": "https://example.com/images/ipadair5.jpg"
        },
        {
            "name": "Google Nest Hub (2nd Gen)",
            "category": "Smart Home",
            "brand": "Google",
            "price": 7999.00,
            "description": "Smart display with Google Assistant and sleep sensing.",
            "image_url": "https://example.com/images/googlenesthub2.jpg"
        },
        {
            "name": "Canon EOS 90D",
            "category": "Camera",
            "brand": "Canon",
            "price": 79999.00,
            "description": "DSLR with 32.5MP sensor and 10 fps continuous shooting.",
            "image_url": "https://example.com/images/canoneos90d.jpg"
        },
        {
            "name": "Samsung Galaxy Tab S8",
            "category": "Tablet",
            "brand": "Samsung",
            "price": 59999.00,
            "description": "High-performance Android tablet with S Pen support.",
            "image_url": "https://example.com/images/galaxytabs8.jpg"
        },
        {
            "name": "Microsoft Surface Pro 9",
            "category": "Tablet",
            "brand": "Microsoft",
            "price": 109999.00,
            "description": "2-in-1 laptop/tablet with Intel Evo platform.",
            "image_url": "https://example.com/images/surfacepro9.jpg"
        },
        {
            "name": "Roku Streaming Stick 4K",
            "category": "Streaming Device",
            "brand": "Roku",
            "price": 4999.00,
            "description": "Compact streaming stick with 4K HDR and voice remote.",
            "image_url": "https://example.com/images/rokustick4k.jpg"
        },
        {
            "name": "Philips Hue White and Color Ambiance",
            "category": "Smart Home",
            "brand": "Philips",
            "price": 12999.00,
            "description": "Smart LED bulbs with full color control and voice compatibility.",
            "image_url": "https://example.com/images/philipshue.jpg"
        },
        {
            "name": "Nikon Z6 II",
            "category": "Camera",
            "brand": "Nikon",
            "price": 159999.00,
            "description": "Mirrorless camera with dual processors and 4K UHD video.",
            "image_url": "https://example.com/images/nikonz6ii.jpg"
        },
        {
            "name": "Logitech MX Master 3",
            "category": "Accessories",
            "brand": "Logitech",
            "price": 9999.00,
            "description": "Advanced wireless mouse with ergonomic design and customizable buttons.",
            "image_url": "https://example.com/images/logitechmxmaster3.jpg"
        },
        {
            "name": "Garmin Forerunner 955",
            "category": "Smartwatch",
            "brand": "Garmin",
            "price": 49999.00,
            "description": "Premium GPS running and triathlon smartwatch with advanced metrics.",
            "image_url": "https://example.com/images/garminforerunner955.jpg"
        },
        {
            "name": "Alienware Aurora R15",
            "category": "Desktop",
            "brand": "Dell",
            "price": 259999.00,
            "description": "High-end gaming desktop with Intel Core i9 and RTX 4090 GPU.",
            "image_url": "https://example.com/images/alienwareaurora.jpg"
        },
        {
            "name": "Samsung T7 Portable SSD",
            "category": "Storage",
            "brand": "Samsung",
            "price": 12999.00,
            "description": "Fast external SSD with up to 1TB capacity and USB-C.",
            "image_url": "https://example.com/images/samsungt7ssd.jpg"
        },
        {
            "name": "DJI Osmo Mobile 6",
            "category": "Accessories",
            "brand": "DJI",
            "price": 15999.00,
            "description": "Handheld smartphone gimbal stabilizer with active tracking.",
            "image_url": "https://example.com/images/djiosmomobile6.jpg"
        },
        {
            "name": "Sony Bravia XR A80K",
            "category": "TV",
            "brand": "Sony",
            "price": 119999.00,
            "description": "OLED 4K Smart TV with Cognitive Processor XR for stunning picture quality.",
            "image_url": "https://example.com/images/sonybraviaa80k.jpg"
        },
        {
            "name": "Echo Dot (5th Gen)",
            "category": "Smart Home",
            "brand": "Amazon",
            "price": 4499.00,
            "description": "Compact smart speaker with Alexa voice assistant.",
            "image_url": "https://example.com/images/echodot5.jpg"
        },
        {
            "name": "Corsair K95 RGB Platinum",
            "category": "Accessories",
            "brand": "Corsair",
            "price": 15999.00,
            "description": "Mechanical gaming keyboard with customizable RGB lighting.",
            "image_url": "https://example.com/images/corsairk95.jpg"
        },
        {
            "name": "Nest Learning Thermostat",
            "category": "Smart Home",
            "brand": "Google",
            "price": 12999.00,
            "description": "Smart thermostat that programs itself and saves energy.",
            "image_url": "https://example.com/images/nestthermostat.jpg"
        },
        {
            "name": "Lenovo Legion 5 Pro",
            "category": "Laptop",
            "brand": "Lenovo",
            "price": 139999.00,
            "description": "Gaming laptop with Ryzen 7 and RTX 3060 GPU, perfect for gamers and creators.",
            "image_url": "https://example.com/images/legion5pro.jpg"
        },
        {
            "name": "Apple AirPods Pro (2nd Gen)",
            "category": "Headphones",
            "brand": "Apple",
            "price": 26999.00,
            "description": "Noise-cancelling wireless earbuds with spatial audio and MagSafe charging.",
            "image_url": "https://example.com/images/airpodspro2.jpg"
        },
        {
            "name": "OnePlus Pad",
            "category": "Tablet",
            "brand": "OnePlus",
            "price": 37999.00,
            "description": "11.6-inch tablet with 144Hz display and MediaTek Dimensity 9000 processor.",
            "image_url": "https://example.com/images/onepluspad.jpg"
        },
        {
            "name": "Sony WH-CH720N",
            "category": "Headphones",
            "brand": "Sony",
            "price": 9999.00,
            "description": "Affordable noise-cancelling over-ear headphones with clear audio.",
            "image_url": "https://example.com/images/sonych720n.jpg"
        },
        {
            "name": "HP Envy x360 15",
            "category": "Laptop",
            "brand": "HP",
            "price": 84999.00,
            "description": "2-in-1 convertible laptop with touch display and AMD Ryzen 5.",
            "image_url": "https://example.com/images/hpenvyx360.jpg"
        },
        {
            "name": "iQOO Neo 7",
            "category": "Smartphone",
            "brand": "iQOO",
            "price": 29999.00,
            "description": "Performance-focused smartphone with Dimensity 8200 and AMOLED display.",
            "image_url": "https://example.com/images/iqooneo7.jpg"
        },
        {
            "name": "Canon PowerShot G7X Mark III",
            "category": "Camera",
            "brand": "Canon",
            "price": 52999.00,
            "description": "Compact vlogging camera with flip-up screen and 4K video support.",
            "image_url": "https://example.com/images/g7xmarkiii.jpg"
        },
        {
            "name": "Realme Narzo N55",
            "category": "Smartphone",
            "brand": "Realme",
            "price": 10999.00,
            "description": "Budget-friendly Android phone with 90Hz display and dual cameras.",
            "image_url": "https://example.com/images/realmenarzon55.jpg"
        },
        {
            "name": "Google Pixel Buds A-Series",
            "category": "Headphones",
            "brand": "Google",
            "price": 7999.00,
            "description": "Wireless earbuds with adaptive sound and Google Assistant.",
            "image_url": "https://example.com/images/pixelbudsa.jpg"
        },
        {
            "name": "Sony ZV-1F Vlogging Camera",
            "category": "Camera",
            "brand": "Sony",
            "price": 44999.00,
            "description": "Compact vlogging camera with background defocus and built-in mic.",
            "image_url": "https://example.com/images/sonyzv1f.jpg"
        },
        {
            "name": "Xiaomi Pad 6",
            "category": "Tablet",
            "brand": "Xiaomi",
            "price": 27999.00,
            "description": "Snapdragon 870 powered tablet with 2.8K display and quad speakers.",
            "image_url": "https://example.com/images/xiaomipad6.jpg"
        },
        {
            "name": "Beats Studio3 Wireless",
            "category": "Headphones",
            "brand": "Beats",
            "price": 19999.00,
            "description": "High-performance headphones with active noise cancelling.",
            "image_url": "https://example.com/images/beatsstudio3.jpg"
        },
        {
            "name": "Nothing Ear (2)",
            "category": "Headphones",
            "brand": "Nothing",
            "price": 9999.00,
            "description": "Unique transparent earbuds with personalized ANC and great sound.",
            "image_url": "https://example.com/images/nothingear2.jpg"
        },
        {
            "name": "Asus ZenBook 14 OLED",
            "category": "Laptop",
            "brand": "ASUS",
            "price": 104999.00,
            "description": "Premium ultrabook with OLED display and Intel Evo platform.",
            "image_url": "https://example.com/images/zenbook14oled.jpg"
        },
        {
            "name": "Dell Inspiron 14 2-in-1",
            "category": "Laptop",
            "brand": "Dell",
            "price": 73999.00,
            "description": "Convertible laptop with touchscreen and stylus support.",
            "image_url": "https://example.com/images/inspiron14.jpg"
        },
        {
            "name": "Amazon Fire HD 10",
            "category": "Tablet",
            "brand": "Amazon",
            "price": 14999.00,
            "description": "Affordable tablet with 10.1\" Full HD screen and Alexa integration.",
            "image_url": "https://example.com/images/firehd10.jpg"
        },
        {
            "name": "Redmi Buds 4 Active",
            "category": "Headphones",
            "brand": "Redmi",
            "price": 1399.00,
            "description": "Budget TWS earbuds with environmental noise cancellation.",
            "image_url": "https://example.com/images/redmibuds4.jpg"
        },
        {
            "name": "DJI Mini 3 Drone",
            "category": "Camera",
            "brand": "DJI",
            "price": 74999.00,
            "description": "Compact drone with 4K HDR video and lightweight design under 249g.",
            "image_url": "https://example.com/images/djimini3.jpg"
        },
        {
            "name": "Lenovo Yoga Smart Tab",
            "category": "Tablet",
            "brand": "Lenovo",
            "price": 19999.00,
            "description": "Android tablet with Google Assistant ambient mode and Dolby Atmos.",
            "image_url": "https://example.com/images/yogasmarttab.jpg"
        },
        {
            "name": "Samsung Galaxy A54 5G",
            "category": "Smartphone",
            "brand": "Samsung",
            "price": 37999.00,
            "description": "Mid-range phone with AMOLED display and long-lasting battery.",
            "image_url": "https://example.com/images/galaxya545g.jpg"
        },
        {
        "name": "MacBook Pro 16-inch M3",
        "category": "Laptop",
        "brand": "Apple",
        "price": 249999.00,
        "description": "High-end MacBook with M3 chip, Liquid Retina XDR display, and all-day battery life.",
        "image_url": "https://example.com/images/macbookpro16m3.jpg"
        },
        {
            "name": "Samsung Galaxy Tab S9 Ultra",
            "category": "Tablet",
            "brand": "Samsung",
            "price": 109999.00,
            "description": "14.6-inch Super AMOLED display with S-Pen support and Snapdragon 8 Gen 2 processor.",
            "image_url": "https://example.com/images/tabs9ultra.jpg"
        },
        {
            "name": "Microsoft Surface Laptop 5",
            "category": "Laptop",
            "brand": "Microsoft",
            "price": 124999.00,
            "description": "Sleek Windows laptop with PixelSense touchscreen and 12th Gen Intel i7.",
            "image_url": "https://example.com/images/surfacelaptop5.jpg"
        },
        {
            "name": "Boat Nirvana 751 ANC",
            "category": "Headphones",
            "brand": "boAt",
            "price": 3999.00,
            "description": "Affordable ANC headphones with 65 hours battery life and immersive sound.",
            "image_url": "https://example.com/images/boatan751.jpg"
        },
        {
            "name": "GoPro Hero 12 Black",
            "category": "Camera",
            "brand": "GoPro",
            "price": 49999.00,
            "description": "Action camera with 5.3K video, improved stabilization, and HDR video.",
            "image_url": "https://example.com/images/goprohero12.jpg"
        },
        {
            "name": "Vivo V29 Pro 5G",
            "category": "Smartphone",
            "brand": "Vivo",
            "price": 38999.00,
            "description": "Stylish phone with curved AMOLED, Sony IMX766 sensor and 66W fast charging.",
            "image_url": "https://example.com/images/vivov29pro.jpg"
        },
        {
            "name": "Huawei MatePad 11.5",
            "category": "Tablet",
            "brand": "Huawei",
            "price": 32999.00,
            "description": "Lightweight HarmonyOS tablet with 2.8K display and detachable keyboard support.",
            "image_url": "https://example.com/images/matepad115.jpg"
        },
        {
            "name": "Marshall Major IV",
            "category": "Headphones",
            "brand": "Marshall",
            "price": 11999.00,
            "description": "Iconic on-ear headphones with 80+ hours of playtime and wireless charging.",
            "image_url": "https://example.com/images/marshallmajor4.jpg"
        },
        {
            "name": "DJI Osmo Pocket 3",
            "category": "Camera",
            "brand": "DJI",
            "price": 34999.00,
            "description": "Portable 4K camera with 3-axis gimbal and face tracking for vlogging.",
            "image_url": "https://example.com/images/osmopocket3.jpg"
        },
        {
            "name": "HP Victus 16",
            "category": "Laptop",
            "brand": "HP",
            "price": 88999.00,
            "description": "Gaming laptop with Intel i5-12450H and RTX 3050 GPU.",
            "image_url": "https://example.com/images/hpvictus16.jpg"
        },
        {
            "name": "Asus ROG Phone 8",
            "category": "Smartphone",
            "brand": "ASUS",
            "price": 79999.00,
            "description": "Gaming smartphone with 165Hz AMOLED display and AeroActive cooling.",
            "image_url": "https://example.com/images/rogphone8.jpg"
        },
        {
            "name": "Nikon Z30 Mirrorless",
            "category": "Camera",
            "brand": "Nikon",
            "price": 63999.00,
            "description": "Compact mirrorless camera perfect for vlogging with 4K and 20.9MP sensor.",
            "image_url": "https://example.com/images/nikonz30.jpg"
        },
        {
            "name": "Redmi Pad SE",
            "category": "Tablet",
            "brand": "Redmi",
            "price": 12999.00,
            "description": "Value tablet with Snapdragon 680 and 11\" FHD display.",
            "image_url": "https://example.com/images/redmipadse.jpg"
        },
        {
            "name": "Realme Buds Wireless 3",
            "category": "Headphones",
            "brand": "Realme",
            "price": 1799.00,
            "description": "Neckband-style Bluetooth earphones with 45dB ANC and 40-hour battery.",
            "image_url": "https://example.com/images/realmewireless3.jpg"
        },
        {
            "name": "Dell G15 Ryzen Edition",
            "category": "Laptop",
            "brand": "Dell",
            "price": 95999.00,
            "description": "Gaming laptop with AMD Ryzen 7 and RTX 4050 GPU.",
            "image_url": "https://example.com/images/dellg15.jpg"
        },
        {
            "name": "Tecno Camon 20 Premier",
            "category": "Smartphone",
            "brand": "Tecno",
            "price": 25999.00,
            "description": "Midrange phone with 108MP sensor and RGBW lens.",
            "image_url": "https://example.com/images/tecno20premier.jpg"
        },
        {
            "name": "Canon EOS R50",
            "category": "Camera",
            "brand": "Canon",
            "price": 74999.00,
            "description": "Entry-level mirrorless camera with APS-C sensor and dual pixel AF.",
            "image_url": "https://example.com/images/eosr50.jpg"
        },
        {
            "name": "Noise Luna Ring",
            "category": "Smartphone",  # Optional: Or Smartwear
            "brand": "Noise",
            "price": 18999.00,
            "description": "Smart ring for health tracking with heart rate and sleep data.",
            "image_url": "https://example.com/images/lunaring.jpg"
        },
        {
            "name": "Samsung Galaxy Buds2 Pro",
            "category": "Headphones",
            "brand": "Samsung",
            "price": 17999.00,
            "description": "Premium TWS earbuds with 24-bit audio and intelligent ANC.",
            "image_url": "https://example.com/images/galaxybuds2pro.jpg"
        },
        {
            "name": "Motorola Edge 50 Pro",
            "category": "Smartphone",
            "brand": "Motorola",
            "price": 31999.00,
            "description": "Curved OLED display, 68W charging, and 144Hz refresh rate.",
            "image_url": "https://example.com/images/edge50pro.jpg"
        },
    ]

    products = [Product(**prod) for prod in products_data]

    db.session.bulk_save_objects(products)
    db.session.commit()

    print("✅ Database initialized with predefined products.")
