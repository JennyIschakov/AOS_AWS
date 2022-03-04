import unittest
import datetime

import adshopcart_methods as methods
import adshopcart_locators as locators


divider = '---------------------------------------------'


class AOSTest(unittest.TestCase):

    @staticmethod
    def test_AOS():
        # Open browser -> navigate to home page -> validate correct URL and title
        methods.setUp()

        # Scenario_01: Register new user and check first sign in with this new registered user
        print(divider)
        print(f'Scenario_01 started at {datetime.datetime.now()}')
        print('Scenario_01: Register new user and check first sign in with this new registered user')

        # Register new user
        methods.register_new_user()

        # Validate details of new registered user - direct after registration
        print(divider)
        print('We validate details of new registered user - direct after registration')
        methods.check_user_account_details()

        # Sign out
        methods.sign_out()

        # Validate sign in of new registered user
        # methods.sign_in()
        print('New user successfully signed in')

        # Validate details of new registered user - after sign in
        print(divider)
        print('We validate details of new registered user - after sign in')
        # methods.check_user_account_details()

        # Delete user - while we are already inside account
        print(divider)
        print('After validating new user details - we delete the account')
        # methods.delete_account()

        # Validate that we are not able to sign in with deleted user
        print(divider)
        print('Validate that we are not able to sign in with deleted user')
        # methods.sign_in()

        # Verification message - Incorrect user name or password.
        # methods.verification_message()

        print(divider)
        print(f'Scenario_01 completed at {datetime.datetime.now()}')

    # ==============================================================================


        # Scenario_02: We check content on home page - links/buttons/contact us form
        print(divider)
        print(f'Scenario_02 started at {datetime.datetime.now()}')
        print('Scenario_02: We check content on home page - links/buttons/contact us form')

        # Validate product categories:
        # 1. category name is displayed/clickable/landed on correct page
        # 2. for each category - Shop now is displayed/clickable/landed on correct page
        # methods.check_product_categories()

        # Validation of navigation top menus: clickable and go to right section
        # methods.check_top_navigation_menu()

        # Validate main logo is displayed
        # methods.main_logo()

        # Validation of CONTACT US form
        # methods.contact_us()

        # Close the web browser
        # methods.tearDown()

        print(divider)
        print(f'Scenario_02 completed at {datetime.datetime.now()}')



