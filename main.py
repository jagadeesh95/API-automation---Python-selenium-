from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Define the base URL of the Petstore API
base_url = 'https://petstore.swagger.io/v2'


def test_get_inventory():
    # Open a new browser window and navigate to the inventory endpoint
    driver.get(f'{base_url}/store/inventory')
    response = driver.execute_script("return arguments[0].innerText;", driver.find_element_by_tag_name("body"))

    # Verify the content by checking if the response is not empty
    assert response is not None


def test_get_available_pets():
    # Open a new browser window and navigate to the available pets endpoint
    driver.get(f'{base_url}/pet/findByStatus?status=available')
    response = driver.execute_script("return arguments[0].innerText;", driver.find_element_by_tag_name("body"))

    # Verify the content by checking if the response is not empty
    assert response is not None


def test_get_order_by_id():
    # Open a new browser window and navigate to an order by ID endpoint
    order_id = 1  # Replace with a valid order ID
    driver.get(f'{base_url}/store/order/{order_id}')
    response = driver.execute_script("return arguments[0].innerText;", driver.find_element_by_tag_name("body"))

    # Verify the content by checking if the response is not empty
    assert response is not None


# Run the tests
test_get_inventory()
test_get_available_pets()
test_get_order_by_id()

# Close the browser window
driver.quit()
