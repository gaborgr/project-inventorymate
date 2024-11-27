## 📦 InventoryMate <img src="https://github.com/user-attachments/assets/377b00ee-8802-447c-aec4-f47754fd9b11" width="120px" />

<div align="center"><img src="https://github.com/user-attachments/assets/e635e71c-8405-42b6-a278-382e3990fe54"  /> </div>

## About the APP
<p>InventoryMate is a Django application designed for inventory management. It allows users to add, modify, and delete product records while providing key insights such as profit margins and the last update timestamp.</p>

## 📋 Features
- Product Management: Add, edit, and delete products.
- Data Insights:
    + Profit margin calculation (sale price vs. last purchase cost).
    + Timestamp of the latest modification.
- User-Friendly Interface: A custom HTML interface designed for simplicity, without relying solely on Django's admin panel.
- Dynamic Database: Automatically updates and stores data with every operation.

## ⚙️ Configuration
The configuration process involves several key steps:
1. **Creating the Application:**
The app, named `product`, is included in the `INSTALLED_APPS` list in the main project settings.

2. **URL Routing:**
Three main routes were created:
    + A route to display the full inventory.
    + A route to show a product entry form.
    + A route for product search and modification.

<div align="center"><img src="https://github.com/user-attachments/assets/ab485997-2b0b-44eb-9d5c-acf43a216cd8"  /> </div>

3. **Database Model:**
A model was designed to structure product data in the database, including fields like name, quantity, sale price, supplier name, last purchase cost, profit margin, and last update timestamp.
Add a screenshot of the model schema here.

<div align="center"><img src="https://github.com/user-attachments/assets/db08008c-13a1-4d6a-8b1d-7ae2b7ff636a"  /> </div>

4. **View Functions:**
Each feature has a dedicated view to handle database interactions and render HTML templates. For example, here’s the view for displaying the complete inventory:

<div align="center"><img src="https://github.com/user-attachments/assets/af97895e-4982-4dc2-8021-79a02516a033"  /> </div>

5. **Base Template for Reusability:**
A `base.html` template was created for consistent styling across the application, extended in all other templates.

## 📷 Screenshots
<div align="center">
  <h4>View All Porducts</h4>
  <img src="https://github.com/user-attachments/assets/67b2a9a4-a870-4518-8861-097405efd2e0"  />
  </div>

<div align="center">
  <h4>Add Porducts</h4>
  <img src="https://github.com/user-attachments/assets/c82002e6-6de9-4d74-888d-098a6644ed2b"  />
</div>

<div align="center">
  <h4>Edit Porducts</h4>
  <img src="https://github.com/user-attachments/assets/bd9c69f4-ab19-48fa-bb0e-eaed2a2c6686"  />
</div>

## 🌟 How to Run
1. Clone this repository.
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run database migrations: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`
5. Access the application at `http://127.0.0.1:8000/`.

## 🤝 Contribution
Feedback is welcome! Fork this repository, make improvements, and submit a pull request. Let’s enhance InventoryMate together.
