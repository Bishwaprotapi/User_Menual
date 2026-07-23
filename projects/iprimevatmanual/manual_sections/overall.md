# primevat: User Manual

**Software purpose:** Generate manual

**Target audience:** client

## 1. Client Integration Module

### Page: Client Integration

![Client Integration: Screen](screenshots/client_integration/client_integration.png)

**Page purpose:** This page provides an interface to view and manage integrated client data across various modules such as Items, Partners, and Transactions.

**Route:** `/client-integration`

<!-- manual-meta: {"module": "Client Integration", "page": "Client Integration", "task": "View integrated item list", "action": "view", "roles": [], "route": "/client-integration", "screenshots": ["screenshots/client_integration/client_integration.png"], "keywords": ["list items", "integration view", "item catalog"], "task_order": 1} -->
#### Task: View integrated item list

**Purpose:** To review the list of items integrated from the client system.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User is logged into Prime VAT
* A company is selected from the top-left dropdown

**Steps:**
1. Navigate to the 'CLIENT INTEGRATION' menu item in the left sidebar.
2. Click on the 'ITEM' tab if not already selected.

**Fields and controls:**
* **SL:** Serial number of the item.
* **Item Code:** Unique identifier for the item.
* **Item Name:** Descriptive name of the item.
* **Item Type:** The classification type of the item.
* **Item Category:** The category the item belongs to.
* **Subcategory:** The specific subcategory of the item.
* **Unit of Measure:** The standard unit used to measure the item.
* **Average Rate:** The calculated average cost or rate for the item.
* **Current Selling Price:** The present market or system selling price.
* **Action:** Available actions for the specific row entry.

**Expected result:** The table populates with integrated item records if available.

**Warnings:**
* No specific warning was identified

**Search keywords:** list items, integration view, item catalog

## 2. Configuration Module

### Page: Branch

![Branch: Screen](screenshots/configuration/branch.png)

**Page purpose:** This page allows the user to manage and view branch locations for the business.

**Route:** `/configuration/businessConfig/branch`

<!-- manual-meta: {"module": "Configuration", "page": "Branch", "task": "Create new branch", "action": "create", "roles": [], "route": "/configuration/businessConfig/branch", "screenshots": ["screenshots/configuration/branch.png"], "keywords": ["add branch", "new office"], "task_order": 1} -->
#### Task: Create new branch

**Purpose:** To add a new branch location to the system.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Must be logged in with appropriate permissions

**Steps:**
1. Navigate to Configuration
2. Select Business Config
3. Click on Branch
4. Click the Create New button

**Fields and controls:**
* **Branch Name:** Name of the branch.
* **Branch Address:** Address details of the branch.

**Expected result:** A new branch is added to the list.

**Warnings:**
* No specific warning was identified

**Search keywords:** add branch, new office

<!-- manual-meta: {"module": "Configuration", "page": "Branch", "task": "View branch list", "action": "view", "roles": [], "route": "/configuration/businessConfig/branch", "screenshots": ["screenshots/configuration/branch.png"], "keywords": ["list branches", "all locations"], "task_order": 2} -->
#### Task: View branch list

**Purpose:** To view all existing business branches.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Configuration
2. Select Business Config
3. Click on Branch

**Fields and controls:**
* **SL:** Serial number.
* **Branch Name:** Name of the branch.
* **Branch Address:** Physical location of the branch.

**Expected result:** A list of branches is displayed.

**Warnings:**
* No specific warning was identified

**Search keywords:** list branches, all locations

### Page: Client Integration

![Business Config: Screen](screenshots/configuration/business_config.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/configuration/businessConfig`

<!-- manual-meta: {"module": "Configuration", "page": "Client Integration", "task": "Use Client Integration", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/configuration/businessConfig", "screenshots": ["screenshots/configuration/business_config.png"], "keywords": ["Client Integration", "business config"], "task_order": 1} -->
#### Task: Use Client Integration

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the Client Integration page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** Client Integration, business config

### Page: Change Password

![Change Password: Screen](screenshots/configuration/change_password.png)

**Page purpose:** Allows users to update their account login credentials.

**Route:** `/configuration/roleManagement/changePassword`

<!-- manual-meta: {"module": "Configuration", "page": "Change Password", "task": "Change user password", "action": "edit", "roles": [], "route": "/configuration/roleManagement/changePassword", "screenshots": ["screenshots/configuration/change_password.png"], "keywords": ["password update", "security"], "task_order": 1} -->
#### Task: Change user password

**Purpose:** To update the current user password for security.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Must know the current password

**Steps:**
1. Navigate to Configuration
2. Select User Management
3. Click Change Password
4. Enter Old Password
5. Enter New Password
6. Enter Confirm Password
7. Click Save

**Fields and controls:**
* **Enter Old Password:** Existing account password.
* **Enter New Password:** New desired password.
* **Enter Confirm Password:** Retype new password for verification.

**Expected result:** Password updated successfully.

**Warnings:**
* No specific warning was identified

**Search keywords:** password update, security

### Page: Client Integration

![Configuration: Screen](screenshots/configuration/configuration.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/configuration`

<!-- manual-meta: {"module": "Configuration", "page": "Client Integration", "task": "Use Client Integration", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/configuration", "screenshots": ["screenshots/configuration/configuration.png"], "keywords": ["Client Integration", "configuration"], "task_order": 1} -->
#### Task: Use Client Integration

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the Client Integration page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** Client Integration, configuration

### Page: User List

![Create User: Screen](screenshots/configuration/create_user.png)

**Page purpose:** Manage system users and access rights.

**Route:** `/configuration/roleManagement/createUser`

<!-- manual-meta: {"module": "Configuration", "page": "User List", "task": "View system users", "action": "view", "roles": [], "route": "/configuration/roleManagement/createUser", "screenshots": ["screenshots/configuration/create_user.png"], "keywords": ["user list", "manage users"], "task_order": 1} -->
#### Task: View system users

**Purpose:** To review the list of registered users and their details.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Configuration
2. Select User Management
3. Click Create User

**Fields and controls:**
* **User (ID):** Unique identifier for the user.
* **User Name:** Full name of the user.
* **Email Address:** Registered email address.
* **Country Name:** Country of the user.
* **Contact Number:** Phone number for the user.

**Expected result:** A table of users is displayed.

**Warnings:**
* No specific warning was identified

**Search keywords:** user list, manage users

### Page: Customer/Supplier Profile

![Customer Supplier: Screen](screenshots/configuration/customer_supplier.png)

**Page purpose:** Central list of all business partners, including customers and suppliers.

**Route:** `/configuration/partnerConfig/partner`

<!-- manual-meta: {"module": "Configuration", "page": "Customer/Supplier Profile", "task": "Filter partners", "action": "filter", "roles": [], "route": "/configuration/partnerConfig/partner", "screenshots": ["screenshots/configuration/customer_supplier.png"], "keywords": ["filter customers", "search suppliers"], "task_order": 1} -->
#### Task: Filter partners

**Purpose:** To find specific partners based on their classification.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Configuration
2. Select Customer/Supplier Config
3. Click Customer/Supplier
4. Select type (All, VDS Applicable, Without VDS Applicable)

**Fields and controls:**
* **Customer/Supplier Name Search:** Keyword search for business name.

**Expected result:** The table content updates to show filtered partners.

**Warnings:**
* No specific warning was identified

**Search keywords:** filter customers, search suppliers

### Page: Unit Of Measurement

![Customer Supplier Config: Screen](screenshots/configuration/customer_supplier_config.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/configuration/partnerConfig`

<!-- manual-meta: {"module": "Configuration", "page": "Unit Of Measurement", "task": "Use Unit Of Measurement", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/configuration/partnerConfig", "screenshots": ["screenshots/configuration/customer_supplier_config.png"], "keywords": ["Unit Of Measurement", "customer supplier config"], "task_order": 1} -->
#### Task: Use Unit Of Measurement

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the Unit Of Measurement page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* **Name & Code Search:** Visible text control.
* **rows per page:** Visible select control.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** Unit Of Measurement, customer supplier config

### Page: Item

![Item: Screen](screenshots/configuration/item.png)

**Page purpose:** Main registry for all items tracked in the system.

**Route:** `/configuration/itemConfig/item`

<!-- manual-meta: {"module": "Configuration", "page": "Item", "task": "Search items", "action": "search", "roles": [], "route": "/configuration/itemConfig/item", "screenshots": ["screenshots/configuration/item.png"], "keywords": ["find item", "item search"], "task_order": 1} -->
#### Task: Search items

**Purpose:** To quickly locate items by category or type.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Configuration
2. Select Item Config
3. Click Item
4. Enter term in Item Type or Category search field

**Fields and controls:**
* **Item Type or Category:** Text box to filter the list.

**Expected result:** The item table updates to match the search query.

**Warnings:**
* No specific warning was identified

**Search keywords:** find item, item search

<!-- manual-meta: {"module": "Configuration", "page": "Item", "task": "Export items", "action": "export", "roles": [], "route": "/configuration/itemConfig/item", "screenshots": ["screenshots/configuration/item.png"], "keywords": ["report", "download excel"], "task_order": 2} -->
#### Task: Export items

**Purpose:** To download the item registry as an Excel file.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Configuration
2. Select Item Config
3. Click Item
4. Click Excel Download

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** File download begins.

**Warnings:**
* No specific warning was identified

**Search keywords:** report, download excel

### Page: Item Category

![Item Category: Screen](screenshots/configuration/item_category.png)

**Page purpose:** This page allows users to view and manage item categories, which help in organizing items within the inventory.

**Route:** `/configuration/itemConfig/itemCategory`

<!-- manual-meta: {"module": "Configuration", "page": "Item Category", "task": "View Item Categories", "action": "view", "roles": [], "route": "/configuration/itemConfig/itemCategory", "screenshots": ["screenshots/configuration/item_category.png"], "keywords": ["category", "item category", "list"], "task_order": 1} -->
#### Task: View Item Categories

**Purpose:** To see a list of existing item categories and their associated codes.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must be logged in

**Steps:**
1. Navigate to CONFIGURATION > Item Config > Item Category
2. View the list displayed in the table

**Fields and controls:**
* **SL:** Serial number of the category.
* **Category Code:** Unique code identifier for the category.
* **Item Type:** The general type of the item.
* **Category Name:** The display name of the category.

**Expected result:** A list of item categories is shown in the table.

**Warnings:**
* No specific warning was identified

**Search keywords:** category, item category, list

<!-- manual-meta: {"module": "Configuration", "page": "Item Category", "task": "Search Item Categories", "action": "search", "roles": [], "route": "/configuration/itemConfig/itemCategory", "screenshots": ["screenshots/configuration/item_category.png"], "keywords": ["filter", "search"], "task_order": 2} -->
#### Task: Search Item Categories

**Purpose:** To quickly locate specific item categories by name or type.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Existing item categories

**Steps:**
1. Navigate to Item Category page
2. Enter the search term into the 'Category Name and Type Search' field

**Fields and controls:**
* **Category Name and Type Search:** Input field for filtering categories.

**Expected result:** The table content is filtered based on the search query.

**Warnings:**
* No specific warning was identified

**Search keywords:** filter, search

### Page: Tax Config

![Item Config: Screen](screenshots/configuration/item_config.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/configuration/itemConfig`

<!-- manual-meta: {"module": "Configuration", "page": "Tax Config", "task": "Use Tax Config", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/configuration/itemConfig", "screenshots": ["screenshots/configuration/item_config.png"], "keywords": ["Tax Config", "item config"], "task_order": 1} -->
#### Task: Use Tax Config

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the Tax Config page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* **returnSubmissionDate:** Visible date control.
* **Representative Designation:** Visible text control.
* **Representative Address:** Visible text control.
* **Bin No:** Visible text control.
* **Busines Unit Address:** Visible text control.
* **Economic Activity Name:** Visible text control.
* **Vat Deduction Source Tax:** Visible checkbox control.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** Tax Config, item config

### Page: Price Declaration

![Price Declaration: Screen](screenshots/configuration/price_declaration.png)

**Page purpose:** This page is used to manage and view price declarations for different items.

**Route:** `/configuration/itemConfig/priceDeclaration`

<!-- manual-meta: {"module": "Configuration", "page": "Price Declaration", "task": "View Price Declarations", "action": "view", "roles": [], "route": "/configuration/itemConfig/priceDeclaration", "screenshots": ["screenshots/configuration/price_declaration.png"], "keywords": ["price", "declaration", "vat"], "task_order": 1} -->
#### Task: View Price Declarations

**Purpose:** To review the pricing details, VAT, and validity dates for items.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to Configuration module

**Steps:**
1. Navigate to CONFIGURATION > Item Config > Price Declaration
2. Browse the table rows

**Fields and controls:**
* **Item Name:** The name of the item declared.
* **Base Price:** The starting price for the item.
* **VAT(%):** VAT percentage applied.
* **Valid From:** Start date of the price declaration.
* **Valid To:** End date of the price declaration.

**Expected result:** A list of price declarations is displayed.

**Warnings:**
* No specific warning was identified

**Search keywords:** price, declaration, vat

### Page: Role Assignment

![Role Assignment: Screen](screenshots/configuration/role_assignment.png)

**Page purpose:** Manages the assignment of roles to users or user groups.

**Route:** `/configuration/roleManagement/roleAssignment`

<!-- manual-meta: {"module": "Configuration", "page": "Role Assignment", "task": "View Role Assignments", "action": "view", "roles": [], "route": "/configuration/roleManagement/roleAssignment", "screenshots": ["screenshots/configuration/role_assignment.png"], "keywords": ["assignment", "role", "user role"], "task_order": 1} -->
#### Task: View Role Assignments

**Purpose:** To audit which users or groups are assigned to specific roles.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User Management permissions

**Steps:**
1. Navigate to CONFIGURATION > User Management > Role Assignment
2. Observe the assigned user groups in the table

**Fields and controls:**
* **User Name / Group:** Identifies the user or the group assigned to a role.

**Expected result:** A table of current role assignments is displayed.

**Warnings:**
* No specific warning was identified

**Search keywords:** assignment, role, user role

### Page: Tafsil

![Tafsil: Screen](screenshots/configuration/tafsil.png)

![Tafsil: Show](screenshots/configuration/tafsil_show.png)

**Page purpose:** Displays detailed VAT and HS Code information for financial and reporting purposes.

**Route:** `/configuration/itemConfig/tafsil`

<!-- manual-meta: {"module": "Configuration", "page": "Tafsil", "task": "Export Tafsil Data", "action": "export", "roles": [], "route": "/configuration/itemConfig/tafsil", "screenshots": ["screenshots/configuration/tafsil.png", "screenshots/configuration/tafsil_show.png"], "keywords": ["export", "excel", "report"], "task_order": 1} -->
#### Task: Export Tafsil Data

**Purpose:** To generate an Excel report of the current schedule data.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Data must be present in the table

**Steps:**
1. Navigate to CONFIGURATION > Item Config > Tafsil
2. Click the 'Export Excel' button

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** An Excel file containing the displayed list is downloaded.

**Warnings:**
* No specific warning was identified

**Search keywords:** export, excel, report

### Page: Tarrif Schedule

![Tarrif Schedule: Screen](screenshots/configuration/tarrif_schedule.png)

![Tarrif Schedule: Show](screenshots/configuration/tarrif_schedule_show.png)

**Page purpose:** Provides a comprehensive view of tariff schedules, including tax rates, CD, RD, SD, and VAT details.

**Route:** `/configuration/itemConfig/tarrifSchedule`

<!-- manual-meta: {"module": "Configuration", "page": "Tarrif Schedule", "task": "View Tariff Schedule", "action": "view", "roles": [], "route": "/configuration/itemConfig/tarrifSchedule", "screenshots": ["screenshots/configuration/tarrif_schedule.png", "screenshots/configuration/tarrif_schedule_show.png"], "keywords": ["tariff", "hs code", "tax"], "task_order": 1} -->
#### Task: View Tariff Schedule

**Purpose:** To review specific tax codes and associated duty rates for the current fiscal year.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None

**Steps:**
1. Navigate to CONFIGURATION > Item Config > Tarrif Schedule
2. Select the 'Fiscal Year' and click 'View'

**Fields and controls:**
* **HS Code:** Harmonized System code for the item.
* **VAT:** Value Added Tax percentage.
* **CD:** Customs Duty rate.

**Expected result:** The tariff table updates to show the selected fiscal year data.

**Warnings:**
* No specific warning was identified

**Search keywords:** tariff, hs code, tax

### Page: Tax Config

![Tax Config: Screen](screenshots/configuration/tax_config.png)

**Page purpose:** Used for configuring fundamental tax-related details for the business.

**Route:** `/configuration/businessConfig/taxConfig`

<!-- manual-meta: {"module": "Configuration", "page": "Tax Config", "task": "Configure Business Tax Details", "action": "configure", "roles": [], "route": "/configuration/businessConfig/taxConfig", "screenshots": ["screenshots/configuration/tax_config.png"], "keywords": ["tax", "bin", "configuration"], "task_order": 1} -->
#### Task: Configure Business Tax Details

**Purpose:** To define organizational tax identifiers and representative contact information.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Admin access

**Steps:**
1. Navigate to CONFIGURATION > Business Config > Tax Config
2. Fill in the required tax fields
3. Review entries before saving

**Fields and controls:**
* **Tax Zone:** Operational tax zone.
* **Tax Circle:** Operational tax circle.
* **Enter Bin No.:** Business Identification Number.

**Expected result:** Tax settings are updated.

**Warnings:**
* No specific warning was identified

**Search keywords:** tax, bin, configuration

### Page: Unit Of Measurement

![Unit Of Measure: Screen](screenshots/configuration/unit_of_measure.png)

**Page purpose:** Lists all defined units of measurement used for items within the system.

**Route:** `/configuration/itemConfig/unitOfMeasure`

<!-- manual-meta: {"module": "Configuration", "page": "Unit Of Measurement", "task": "View Units of Measurement", "action": "view", "roles": [], "route": "/configuration/itemConfig/unitOfMeasure", "screenshots": ["screenshots/configuration/unit_of_measure.png"], "keywords": ["uom", "unit", "measurement"], "task_order": 1} -->
#### Task: View Units of Measurement

**Purpose:** To check available units for item creation.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None

**Steps:**
1. Navigate to CONFIGURATION > Item Config > Unit Of Measure
2. Review the table for existing units

**Fields and controls:**
* **Unit Of Measurement:** Name of the unit (e.g., Ton, Set, Pice).
* **Unit Of Measurement Code:** Abbreviated code for the unit.

**Expected result:** A full list of measurement units is displayed.

**Warnings:**
* No specific warning was identified

**Search keywords:** uom, unit, measurement

### Page: Customer/Supplier Profile

![User Management: Screen](screenshots/configuration/user_management.png)

**Page purpose:** This page displays a list of customer and supplier profiles, allowing for filtering, searching, and viewing of business records.

**Route:** `/configuration/roleManagement`

<!-- manual-meta: {"module": "Configuration", "page": "Customer/Supplier Profile", "task": "Filter Customer/Supplier list", "action": "filter", "roles": [], "route": "/configuration/roleManagement", "screenshots": ["screenshots/configuration/user_management.png"], "keywords": ["VDS", "filter", "partner status"], "task_order": 1} -->
#### Task: Filter Customer/Supplier list

**Purpose:** To narrow down the list of partners by their VDS status.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has access to the Configuration module

**Steps:**
1. Navigate to Configuration
2. Click on User Management
3. Select one of the radio buttons: 'All', 'VDS Applicable', or 'Without VDS Applicable'

**Fields and controls:**
* **Customer/Supplier Type:** Radio button group to filter by VDS status.

**Expected result:** The table displays only records matching the selected VDS criteria.

**Warnings:**
* No specific warning was identified

**Search keywords:** VDS, filter, partner status

<!-- manual-meta: {"module": "Configuration", "page": "Customer/Supplier Profile", "task": "Search for a profile", "action": "search", "roles": [], "route": "/configuration/roleManagement", "screenshots": ["screenshots/configuration/user_management.png"], "keywords": ["search", "find business"], "task_order": 2} -->
#### Task: Search for a profile

**Purpose:** To find a specific customer or supplier record by name.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User is on the Customer/Supplier Profile page

**Steps:**
1. Click into the 'Customer/Supplier Name Search' field
2. Type the name of the business entity
3. Press Enter or wait for the system to filter the table

**Fields and controls:**
* **Customer/Supplier Name Search:** Text input for searching by business name.

**Expected result:** The table updates to show only the entries matching the search term.

**Warnings:**
* No specific warning was identified

**Search keywords:** search, find business

### Page: Role Extension

![User Role Extension: Screen](screenshots/configuration/user_role_extension.png)

**Page purpose:** This page manages the extension of user roles and their associated business units.

**Route:** `/configuration/roleManagement/roleExtension`

<!-- manual-meta: {"module": "Configuration", "page": "Role Extension", "task": "Search for an employee", "action": "search", "roles": [], "route": "/configuration/roleManagement/roleExtension", "screenshots": ["screenshots/configuration/user_role_extension.png"], "keywords": ["search employee", "role extension search"], "task_order": 1} -->
#### Task: Search for an employee

**Purpose:** To locate a specific employee in the role extension list.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User is on the Role Extension page

**Steps:**
1. Locate the 'Employee Name Search' input field
2. Enter the employee name or part of the name
3. Observe the filtered list in the table

**Fields and controls:**
* **Employee Name Search:** Field to search for employees by name.

**Expected result:** The list updates to show only employees matching the search criteria.

**Warnings:**
* No specific warning was identified

**Search keywords:** search employee, role extension search

### Page: Vehicle

![Vehicle: Screen](screenshots/configuration/vehicle.png)

**Page purpose:** This page lists vehicles and allows users to manage or search for vehicle details.

**Route:** `/configuration/vehicleManagement/vehicle`

<!-- manual-meta: {"module": "Configuration", "page": "Vehicle", "task": "Search for a vehicle", "action": "search", "roles": [], "route": "/configuration/vehicleManagement/vehicle", "screenshots": ["screenshots/configuration/vehicle.png"], "keywords": ["find vehicle", "vehicle search"], "task_order": 1} -->
#### Task: Search for a vehicle

**Purpose:** To find a specific vehicle by its number or code.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User is on the Vehicle configuration page

**Steps:**
1. Go to Configuration > Vehicle Management > Vehicle
2. Enter the vehicle number or code into the 'Vehicle No & Code' search field
3. The table automatically refreshes to show the relevant vehicle

**Fields and controls:**
* **Vehicle No & Code:** Search input to filter vehicles by identifier.

**Expected result:** The list of vehicles is narrowed down to the matching record.

**Warnings:**
* No specific warning was identified

**Search keywords:** find vehicle, vehicle search

### Page: Role Extension

![Vehicle Management: Screen](screenshots/configuration/vehicle_management.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/configuration/vehicleManagement`

<!-- manual-meta: {"module": "Configuration", "page": "Role Extension", "task": "Use Role Extension", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/configuration/vehicleManagement", "screenshots": ["screenshots/configuration/vehicle_management.png"], "keywords": ["Role Extension", "vehicle management"], "task_order": 1} -->
#### Task: Use Role Extension

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the Role Extension page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* **Employee Name Search:** Visible text control.
* **rows per page:** Visible select control.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** Role Extension, vehicle management

## 3. Operation Module

### Page: Contract Manufacturing Issue

![Contract Manufacturing Issue: Screen](screenshots/operation/contract_manufacturing_issue.png)

![Contract Manufacturing Issue: Show](screenshots/operation/contract_manufacturing_issue_show.png)

**Page purpose:** This page is used to view and manage raw materials issued for contract manufacturing processes.

**Route:** `/operation/manufacturing/contactManufacturing`

<!-- manual-meta: {"module": "Operation", "page": "Contract Manufacturing Issue", "task": "View Contract Manufacturing Issues", "action": "view", "roles": [], "route": "/operation/manufacturing/contactManufacturing", "screenshots": ["screenshots/operation/contract_manufacturing_issue.png", "screenshots/operation/contract_manufacturing_issue_show.png"], "keywords": ["manufacturing", "issue", "raw material", "contract"], "task_order": 1} -->
#### Task: View Contract Manufacturing Issues

**Purpose:** To list contract manufacturing issue records for a specific date range and branch.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Manufacturing module

**Steps:**
1. Navigate to Operation > Manufacturing > Contract Manufacturing Issue
2. Select the Branch from the dropdown
3. Select the 'From Date'
4. Select the 'To Date'
5. Select the Issue Type
6. Click the 'View' button

**Fields and controls:**
* **Branch:** Select the relevant branch office.
* **From Date:** Starting date for the record search.
* **To Date:** Ending date for the record search.
* **Issue Type:** Type of manufacturing issue (e.g., Issue Raw Material).

**Expected result:** A table displaying records matching the specified filter criteria appears.

**Warnings:**
* No specific warning was identified

**Search keywords:** manufacturing, issue, raw material, contract

### Page: Contract Manufacturing Receive

![Contract Manufacturing Receive: Screen](screenshots/operation/contract_manufacturing_receive.png)

![Contract Manufacturing Receive: Show](screenshots/operation/contract_manufacturing_receive_show.png)

**Page purpose:** This page is used to manage the receipt of raw materials back from contract manufacturing.

**Route:** `/operation/manufacturing/contactMFGReceive`

<!-- manual-meta: {"module": "Operation", "page": "Contract Manufacturing Receive", "task": "View Contract Manufacturing Receipts", "action": "view", "roles": [], "route": "/operation/manufacturing/contactMFGReceive", "screenshots": ["screenshots/operation/contract_manufacturing_receive.png", "screenshots/operation/contract_manufacturing_receive_show.png"], "keywords": ["receive", "raw material", "manufacturing", "receipt"], "task_order": 1} -->
#### Task: View Contract Manufacturing Receipts

**Purpose:** To view records of raw materials received from contract manufacturing.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Manufacturing module

**Steps:**
1. Navigate to Operation > Manufacturing > Contract Manufacturing Receive
2. Select the Branch
3. Define the date range using 'From Date' and 'To Date'
4. Select the Receive Type
5. Click the 'View' button

**Fields and controls:**
* **Branch:** The branch associated with the receipt.
* **From Date:** Beginning of the date range.
* **To Date:** End of the date range.
* **Receive Type:** The category of receipt (e.g., Receive Raw Material).

**Expected result:** A list of receipt transactions is displayed in the table.

**Warnings:**
* No specific warning was identified

**Search keywords:** receive, raw material, manufacturing, receipt

### Page: Credit Note

![Credit Note: Screen](screenshots/operation/credit_note.png)

**Page purpose:** This page allows users to view and search for sales credit notes.

**Route:** `/operation/sales/credit-note`

<!-- manual-meta: {"module": "Operation", "page": "Credit Note", "task": "Search Credit Notes", "action": "search", "roles": [], "route": "/operation/sales/credit-note", "screenshots": ["screenshots/operation/credit_note.png"], "keywords": ["credit note", "sales", "invoice"], "task_order": 1} -->
#### Task: Search Credit Notes

**Purpose:** To filter and locate specific credit notes issued to customers.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Sales module

**Steps:**
1. Navigate to Operation > Sales > Credit Note
2. Select the Branch
3. Set the 'Form Date' and 'To Date'
4. Enter a value in the 'Sales Invoice Search' field
5. Click the 'View' button

**Fields and controls:**
* **Branch:** Select the branch for the credit note.
* **Form Date:** Start date for the search.
* **To Date:** End date for the search.
* **Sales Invoice Search:** Keyword search for specific sales invoices.

**Expected result:** Credit note records matching the search criteria are displayed.

**Warnings:**
* No specific warning was identified

**Search keywords:** credit note, sales, invoice

### Page: Debit Note

![Debit Note: Screen](screenshots/operation/debit_note.png)

![Debit Note: Show](screenshots/operation/debit_note_show.png)

**Page purpose:** This page is used to view and search for purchase-related debit notes.

**Route:** `/operation/purchase/debit-note`

<!-- manual-meta: {"module": "Operation", "page": "Debit Note", "task": "View Debit Notes", "action": "view", "roles": [], "route": "/operation/purchase/debit-note", "screenshots": ["screenshots/operation/debit_note.png", "screenshots/operation/debit_note_show.png"], "keywords": ["debit note", "purchase", "invoice"], "task_order": 1} -->
#### Task: View Debit Notes

**Purpose:** To list debit notes associated with purchase invoices.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Purchase module

**Steps:**
1. Navigate to Operation > Purchase > Debit Note
2. Select the Branch Name
3. Specify the date range
4. Click the 'View' button

**Fields and controls:**
* **Branch Name:** Select the relevant branch.
* **Form Date:** Start date for reporting.
* **To Date:** End date for reporting.
* **Purchase Invoice Search:** Search for specific purchase invoices.

**Expected result:** The table populates with debit note details based on search filters.

**Warnings:**
* No specific warning was identified

**Search keywords:** debit note, purchase, invoice

### Page: Vehicle

![Inventory Transaction: Screen](screenshots/operation/inventory_transaction.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/operation/inventoryTransaction`

<!-- manual-meta: {"module": "Operation", "page": "Vehicle", "task": "Use Vehicle", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/operation/inventoryTransaction", "screenshots": ["screenshots/operation/inventory_transaction.png"], "keywords": ["Vehicle", "inventory transaction"], "task_order": 1} -->
#### Task: Use Vehicle

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the Vehicle page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* **Vehicle No & Code:** Visible text control.
* **rows per page:** Visible select control.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** Vehicle, inventory transaction

### Page: Item Destroy

![Item Destroy: Screen](screenshots/operation/item_destroy.png)

![Item Destroy: Show](screenshots/operation/item_destroy_show.png)

**Page purpose:** This page is used to manage records of items that have been destroyed or written off.

**Route:** `/operation/inventoryTransaction/itemDestroy`

<!-- manual-meta: {"module": "Operation", "page": "Item Destroy", "task": "View Destroyed Items", "action": "view", "roles": [], "route": "/operation/inventoryTransaction/itemDestroy", "screenshots": ["screenshots/operation/item_destroy.png", "screenshots/operation/item_destroy_show.png"], "keywords": ["item destroy", "write off", "inventory"], "task_order": 1} -->
#### Task: View Destroyed Items

**Purpose:** To see a report of items destroyed within a specified date range.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Inventory Transaction module

**Steps:**
1. Navigate to Operation > Inventory Transaction > Item Destroy
2. Select the Branch Name
3. Set the 'From Date' and 'To Date'
4. Select the Item Type
5. Click the 'View' button

**Fields and controls:**
* **Branch Name:** Select the branch for inventory tracking.
* **From Date:** Start date for the list.
* **To Date:** End date for the list.
* **Item Type:** Category of the items (e.g., Purchase Book Item).

**Expected result:** Displays a filtered list of destroyed items.

**Warnings:**
* No specific warning was identified

**Search keywords:** item destroy, write off, inventory

### Page: Transfer Out

![Manufacturing: Screen](screenshots/operation/manufacturing.png)

![Manufacturing: Show](screenshots/operation/manufacturing_show.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/operation/manufacturing`

<!-- manual-meta: {"module": "Operation", "page": "Transfer Out", "task": "Use Transfer Out", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/operation/manufacturing", "screenshots": ["screenshots/operation/manufacturing.png", "screenshots/operation/manufacturing_show.png"], "keywords": ["Transfer Out", "manufacturing"], "task_order": 1} -->
#### Task: Use Transfer Out

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the Transfer Out page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* **Transfer No Search:** Visible text control.
* **rows per page:** Visible select control.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** Transfer Out, manufacturing

### Page: Vehicle

![Operation: Screen](screenshots/operation/operation.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/operation`

<!-- manual-meta: {"module": "Operation", "page": "Vehicle", "task": "Use Vehicle", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/operation", "screenshots": ["screenshots/operation/operation.png"], "keywords": ["Vehicle", "operation"], "task_order": 1} -->
#### Task: Use Vehicle

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the Vehicle page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* **Vehicle No & Code:** Visible text control.
* **rows per page:** Visible select control.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** Vehicle, operation

### Page: Price Declaration Wastage

![Price Declaration Wastage: Screen](screenshots/operation/price_declaration_wastage.png)

**Page purpose:** This page displays a list of wastage price declarations, showing validity dates, total quantities, and prices.

**Route:** `/operation/wastageManagement/priceDeclarationWastage`

<!-- manual-meta: {"module": "Operation", "page": "Price Declaration Wastage", "task": "View price declaration wastage list", "action": "view", "roles": [], "route": "/operation/wastageManagement/priceDeclarationWastage", "screenshots": ["screenshots/operation/price_declaration_wastage.png"], "keywords": ["wastage", "price declaration"], "task_order": 1} -->
#### Task: View price declaration wastage list

**Purpose:** To see the registered wastage price declaration records.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has access to the Wastage Management module.

**Steps:**
1. Navigate to Operation > Wastage Management > Price Declaration Wastage.

**Fields and controls:**
* **SL:** Serial number of the entry.
* **Valid From Date:** Start date of the wastage price declaration.
* **Valid To Date:** End date of the wastage price declaration.
* **Total Qty.:** Total quantity of wastage items.
* **Total Price:** The total declared price value.

**Expected result:** A table showing current and historical wastage price declarations.

**Warnings:**
* No specific warning was identified

**Search keywords:** wastage, price declaration

### Page: Production

![Production: Screen](screenshots/operation/production.png)

![Production: Show](screenshots/operation/production_show.png)

**Page purpose:** This page allows users to view and search for production records within a selected branch and date range.

**Route:** `/operation/manufacturing/production`

<!-- manual-meta: {"module": "Operation", "page": "Production", "task": "Search production records", "action": "search", "roles": [], "route": "/operation/manufacturing/production", "screenshots": ["screenshots/operation/production.png", "screenshots/operation/production_show.png"], "keywords": ["production", "manufacturing", "filter"], "task_order": 1} -->
#### Task: Search production records

**Purpose:** To find specific production records by branch and date.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User is authorized to view Manufacturing data.

**Steps:**
1. Navigate to Operation > Manufacturing > Production.
2. Select the Branch Name.
3. Enter or select the Form Date and To Date.
4. Click the View button.

**Fields and controls:**
* **Branch Name:** The specific branch to filter by.
* **Form Date:** Beginning of the search date range.
* **To Date:** End of the search date range.
* **Production No. Search:** Field to filter by a specific production number.

**Expected result:** A list of production entries matching the selected criteria will be displayed in the table.

**Warnings:**
* No specific warning was identified

**Search keywords:** production, manufacturing, filter

### Page: Purchase

![Purchase: Screen](screenshots/operation/purchase.png)

![Purchase: Show](screenshots/operation/purchase_show.png)

**Page purpose:** This page displays purchase invoice records and allows users to manage or search for them.

**Route:** `/operation/purchase/purchase`

<!-- manual-meta: {"module": "Operation", "page": "Purchase", "task": "View purchase list", "action": "view", "roles": [], "route": "/operation/purchase/purchase", "screenshots": ["screenshots/operation/purchase.png", "screenshots/operation/purchase_show.png"], "keywords": ["purchase", "invoice", "procurement"], "task_order": 1} -->
#### Task: View purchase list

**Purpose:** To review existing purchase invoices for a specific branch and time period.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must have access to the Purchase module.

**Steps:**
1. Navigate to Operation > Purchase > Purchase.
2. Select the branch from the Select Branch field.
3. Set the Enter From Date and Enter To Date.
4. Click View.

**Fields and controls:**
* **Select Branch:** The operational branch to view.
* **Enter From Date:** Start of the date filter.
* **Enter To Date:** End of the date filter.
* **BOE, BIN, Supplier Search:** Search input for specific invoices or suppliers.

**Expected result:** The purchase invoice table is populated with records matching the criteria.

**Warnings:**
* No specific warning was identified

**Search keywords:** purchase, invoice, procurement

### Page: Purchase

![Sales: Screen](screenshots/operation/sales.png)

![Sales: Show](screenshots/operation/sales_show.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/operation/sales`

<!-- manual-meta: {"module": "Operation", "page": "Purchase", "task": "Use Purchase", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/operation/sales", "screenshots": ["screenshots/operation/sales.png", "screenshots/operation/sales_show.png"], "keywords": ["Purchase", "sales"], "task_order": 1} -->
#### Task: Use Purchase

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the Purchase page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* **From Date:** Visible date control.
* **To Date:** Visible date control.
* **BOE, BIN, Supplier Search:** Visible text control.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** Purchase, sales

### Page: Sales Invoice

![Sales Invoice: Screen](screenshots/operation/sales_invoice.png)

![Sales Invoice: Show](screenshots/operation/sales_invoice_show.png)

**Page purpose:** This page provides a search and display interface for all sales invoices recorded in the system.

**Route:** `/operation/sales/salesInvoice`

<!-- manual-meta: {"module": "Operation", "page": "Sales Invoice", "task": "Search sales invoices", "action": "search", "roles": [], "route": "/operation/sales/salesInvoice", "screenshots": ["screenshots/operation/sales_invoice.png", "screenshots/operation/sales_invoice_show.png"], "keywords": ["sales", "invoice", "billing"], "task_order": 1} -->
#### Task: Search sales invoices

**Purpose:** To locate specific sales invoice records.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has access to Sales module.

**Steps:**
1. Navigate to Operation > Sales > Sales Invoice.
2. Select a branch in the Select Branch field.
3. Define the period using the From Date and To Date pickers.
4. Click the View button.

**Fields and controls:**
* **Select Branch:** Filtering by branch.
* **From Date:** Beginning of the invoice date range.
* **To Date:** End of the invoice date range.
* **BOE, BIN, Inv No Search:** Find specific invoices by reference.

**Expected result:** Relevant sales invoices are shown in the table below.

**Warnings:**
* No specific warning was identified

**Search keywords:** sales, invoice, billing

### Page: Transfer In

![Transfer In: Screen](screenshots/operation/transfer_in.png)

![Transfer In: Show](screenshots/operation/transfer_in_show.png)

**Page purpose:** This page lists inventory items that have been transferred into the branch.

**Route:** `/operation/inventoryTransaction/transferIn`

<!-- manual-meta: {"module": "Operation", "page": "Transfer In", "task": "Filter transfer-in records", "action": "filter", "roles": [], "route": "/operation/inventoryTransaction/transferIn", "screenshots": ["screenshots/operation/transfer_in.png", "screenshots/operation/transfer_in_show.png"], "keywords": ["transfer", "inventory", "stock"], "task_order": 1} -->
#### Task: Filter transfer-in records

**Purpose:** To narrow down inventory transfers into the branch.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has access to Inventory Transaction.

**Steps:**
1. Navigate to Operation > Inventory Transaction > Transfer In.
2. Select the Branch Name.
3. Select the Item Type.
4. Click the View button.

**Fields and controls:**
* **Branch Name:** The target branch for the transfer-in.
* **Item Type:** Category of the inventory being transferred.
* **Transfer-In No Search:** Search by transfer number.

**Expected result:** Inventory Transfer-In records matching the selection are displayed.

**Warnings:**
* No specific warning was identified

**Search keywords:** transfer, inventory, stock

### Page: Transfer Out

![Transfer Out: Screen](screenshots/operation/transfer_out.png)

![Transfer Out: Show](screenshots/operation/transfer_out_show.png)

**Page purpose:** This page displays details of inventory transferred out from the current branch to another destination.

**Route:** `/operation/inventoryTransaction/transferOut`

<!-- manual-meta: {"module": "Operation", "page": "Transfer Out", "task": "View transfer-out details", "action": "view", "roles": [], "route": "/operation/inventoryTransaction/transferOut", "screenshots": ["screenshots/operation/transfer_out.png", "screenshots/operation/transfer_out_show.png"], "keywords": ["transfer", "outbound", "stock"], "task_order": 1} -->
#### Task: View transfer-out details

**Purpose:** To review the history and details of outgoing inventory transfers.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has access to the Inventory Transaction module.

**Steps:**
1. Navigate to Operation > Inventory Transaction > Transfer Out.
2. Select the Branch Name.
3. Select the Item Type.
4. Click View.

**Fields and controls:**
* **Branch Name:** Source branch of the items.
* **Item Type:** The type of inventory items.
* **Transfer No Search:** Search by specific transfer record number.

**Expected result:** A table showing transfers to other locations including destination, address, vehicle info, and date.

**Warnings:**
* No specific warning was identified

**Search keywords:** transfer, outbound, stock

### Page: Wastage In

![Wastage In: Screen](screenshots/operation/wastage_in.png)

![Wastage In: Show](screenshots/operation/wastage_in_show.png)

**Page purpose:** This page allows users to view records of wastage brought into the facility.

**Route:** `/operation/wastageManagement/wastageIn`

<!-- manual-meta: {"module": "Operation", "page": "Wastage In", "task": "Search wastage in records", "action": "search", "roles": [], "route": "/operation/wastageManagement/wastageIn", "screenshots": ["screenshots/operation/wastage_in.png", "screenshots/operation/wastage_in_show.png"], "keywords": ["wastage", "waste", "management"], "task_order": 1} -->
#### Task: Search wastage in records

**Purpose:** To review records of incoming waste items.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has access to the Wastage Management module.

**Steps:**
1. Navigate to Operation > Wastage Management > Wastage In.
2. Select the Branch.
3. Specify the date range in From Date and To Date.
4. Click View.

**Fields and controls:**
* **Select Branch:** The branch where the wastage was received.
* **From Date:** Beginning of the record search period.
* **To Date:** End of the record search period.

**Expected result:** Records of incoming wastage items are displayed in the list.

**Warnings:**
* No specific warning was identified

**Search keywords:** wastage, waste, management

### Page: Sales Invoice

![Wastage Management: Screen](screenshots/operation/wastage_management.png)

![Wastage Management: Show](screenshots/operation/wastage_management_show.png)

**Page purpose:** Used to view and manage sales invoices under the wastage management module.

**Route:** `/operation/wastageManagement`

<!-- manual-meta: {"module": "Operation", "page": "Sales Invoice", "task": "View Sales Invoices", "action": "view", "roles": [], "route": "/operation/wastageManagement", "screenshots": ["screenshots/operation/wastage_management.png", "screenshots/operation/wastage_management_show.png"], "keywords": ["sales", "invoice", "list", "view"], "task_order": 1} -->
#### Task: View Sales Invoices

**Purpose:** To list and review sales invoices within a specific date range and branch.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has access to the Operation module

**Steps:**
1. Navigate to Operation > Wastage Management
2. Select a branch from the Select Branch dropdown
3. Enter or select the From Date
4. Enter or select the To Date
5. Click the View button

**Fields and controls:**
* **Select Branch:** Dropdown to filter by business branch.
* **Enter From Date:** Start date for the invoice search.
* **Enter To Date:** End date for the invoice search.

**Expected result:** A table list of sales invoices matching the criteria will appear.

**Warnings:**
* No specific warning was identified

**Search keywords:** sales, invoice, list, view

<!-- manual-meta: {"module": "Operation", "page": "Sales Invoice", "task": "Search Sales Invoices", "action": "search", "roles": [], "route": "/operation/wastageManagement", "screenshots": ["screenshots/operation/wastage_management.png", "screenshots/operation/wastage_management_show.png"], "keywords": ["search", "find", "BOE", "BIN"], "task_order": 2} -->
#### Task: Search Sales Invoices

**Purpose:** To find specific sales invoices using invoice identifiers.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has access to the Operation module

**Steps:**
1. Navigate to Operation > Wastage Management
2. Enter a BOE, BIN, or Invoice Number in the search field
3. Click the search icon

**Fields and controls:**
* **BOE, BIN, Inv No Search:** Search input for specific document numbers.

**Expected result:** The table will update to show the matching invoice record.

**Warnings:**
* No specific warning was identified

**Search keywords:** search, find, BOE, BIN

### Page: Wastage Sales

![Wastage Sales: Screen](screenshots/operation/wastage_sales.png)

![Wastage Sales: Show](screenshots/operation/wastage_sales_show.png)

**Page purpose:** Used to view and manage sales invoices related to wastage operations.

**Route:** `/operation/wastageManagement/wastageSalesInvoice`

<!-- manual-meta: {"module": "Operation", "page": "Wastage Sales", "task": "View Wastage Sales", "action": "view", "roles": [], "route": "/operation/wastageManagement/wastageSalesInvoice", "screenshots": ["screenshots/operation/wastage_sales.png", "screenshots/operation/wastage_sales_show.png"], "keywords": ["wastage", "sales", "report"], "task_order": 1} -->
#### Task: View Wastage Sales

**Purpose:** To view the list of wastage sales records for a selected branch and period.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User is logged in
* Access to wastage sales module

**Steps:**
1. Navigate to Operation > Wastage Management > Wastage Sales
2. Select the branch
3. Select the date range using From Date and To Date fields
4. Click the View button

**Fields and controls:**
* **Select Branch:** Branch selector.
* **Enter From Date:** Beginning of the reporting period.
* **Enter To Date:** End of the reporting period.

**Expected result:** The wastage sales table will be populated with invoice data.

**Warnings:**
* No specific warning was identified

**Search keywords:** wastage, sales, report

## 4. Reports Module

### Page: Audit Report

![Audit Report: Screen](screenshots/reports/audit_report.png)

**Page purpose:** This page provides a centralized hub to access various import, purchase, sales, and export audit data records.

**Route:** `/reports/otherReports/auditReport`

<!-- manual-meta: {"module": "Reports", "page": "Audit Report", "task": "View audit report categories", "action": "view", "roles": [], "route": "/reports/otherReports/auditReport", "screenshots": ["screenshots/reports/audit_report.png"], "keywords": ["audit", "import", "purchase", "sales", "export"], "task_order": 1} -->
#### Task: View audit report categories

**Purpose:** To navigate to specific audit report areas including Imports, Local Purchases, Local Sales, and Exports.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Reports module

**Steps:**
1. Navigate to the Reports module in the sidebar.
2. Select 'Audit Report' from the MIS Report list.
3. Click on the desired category button (Import, Local Purchase, Local Sales, or Export) to view associated reports.

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** The user is directed to the relevant audit report dashboard based on the selected category.

**Warnings:**
* No specific warning was identified

**Search keywords:** audit, import, purchase, sales, export

### Page: Chok Ka/Kha Report

![Chok Ka Kha: Screen](screenshots/reports/chok_ka_kha.png)

![Chok Ka Kha: Show](screenshots/reports/chok_ka_kha_show.png)

**Page purpose:** This report displays financial data for Chok Ka and Chok Kha forms for a specified branch and date range.

**Route:** `/reports/otherReports/chok-ka/kha`

<!-- manual-meta: {"module": "Reports", "page": "Chok Ka/Kha Report", "task": "Filter Chok Ka/Kha records", "action": "filter", "roles": [], "route": "/reports/otherReports/chok-ka/kha", "screenshots": ["screenshots/reports/chok_ka_kha.png", "screenshots/reports/chok_ka_kha_show.png"], "keywords": ["chok ka", "chok kha", "financial report", "vat form"], "task_order": 1} -->
#### Task: Filter Chok Ka/Kha records

**Purpose:** To retrieve specific financial records for a given branch and time period.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must have access to the MIS Reports section.

**Steps:**
1. Navigate to 'Chok Ka/Kha' under the MIS Report section.
2. Select the desired branch from the 'Branch' dropdown.
3. Enter or select the 'From Date' and 'To Date'.
4. Click the 'View' button.

**Fields and controls:**
* **Branch:** Dropdown to select the organization branch.
* **From Date:** Date picker for the start of the report period.
* **To Date:** Date picker for the end of the report period.

**Expected result:** The report displays data if found, or displays a 'No Data Found' warning if the selection criteria yield no results.

**Warnings:**
* No specific warning was identified

**Search keywords:** chok ka, chok kha, financial report, vat form

### Page: Credit Note Report

![Credit Note Report: Screen](screenshots/reports/credit_note_report.png)

![Credit Note Report: Show](screenshots/reports/credit_note_report_show.png)

**Page purpose:** This page allows users to view a list of credit notes issued to partners within a specific branch and time frame.

**Route:** `/reports/otherReports/creditNoteReport`

<!-- manual-meta: {"module": "Reports", "page": "Credit Note Report", "task": "Search credit note records", "action": "search", "roles": [], "route": "/reports/otherReports/creditNoteReport", "screenshots": ["screenshots/reports/credit_note_report.png", "screenshots/reports/credit_note_report_show.png"], "keywords": ["credit note", "invoice", "vat correction"], "task_order": 1} -->
#### Task: Search credit note records

**Purpose:** To view credit notes for specific branches and date ranges.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Authorized access to reports.

**Steps:**
1. Select 'Credit Note Report' from the sidebar.
2. Select the 'Branch Name'.
3. Define the 'From Date' and 'To Date'.
4. Click the 'View' button.

**Fields and controls:**
* **Branch Name:** The branch context for the credit notes.
* **From Date:** Start date for transaction filtering.
* **To Date:** End date for transaction filtering.

**Expected result:** A table populated with credit note details such as Partner, Invoice, Fiscal Year, and Transaction Date appears below the search form.

**Warnings:**
* No specific warning was identified

**Search keywords:** credit note, invoice, vat correction

### Page: Debit Note Report

![Debit Note Report: Screen](screenshots/reports/debit_note_report.png)

![Debit Note Report: Show](screenshots/reports/debit_note_report_show.png)

**Page purpose:** This page provides a filtered view of debit notes issued, enabling users to verify transaction history.

**Route:** `/reports/otherReports/debitNoteReport`

<!-- manual-meta: {"module": "Reports", "page": "Debit Note Report", "task": "View debit note report", "action": "view", "roles": [], "route": "/reports/otherReports/debitNoteReport", "screenshots": ["screenshots/reports/debit_note_report.png", "screenshots/reports/debit_note_report_show.png"], "keywords": ["debit note", "transaction history"], "task_order": 1} -->
#### Task: View debit note report

**Purpose:** To extract and verify debit note information for accounting purposes.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must have navigate access to the MIS reports.

**Steps:**
1. Select 'Debit Note Report' from the navigation menu.
2. Choose a 'Branch Name'.
3. Specify the date range using 'From Date' and 'To Date'.
4. Click 'View' to trigger the data pull.

**Fields and controls:**
* **Branch Name:** Identifier for the business entity branch.
* **From Date:** The date from which to start the report.
* **To Date:** The date at which the report ends.

**Expected result:** A populated report table including SL, Branch Name, Partner, Invoice, Fiscal Year, and Transaction Date.

**Warnings:**
* No specific warning was identified

**Search keywords:** debit note, transaction history

### Page: Doc Verification System (DVS)

![Doc Verification System Dvs: Screen](screenshots/reports/doc_verification_system_dvs.png)

**Page purpose:** This page allows users to access the Document Verification System for validating financial and tax-related documents.

**Route:** `/reports/otherReports/docVerificationSystem(DVS)`

<!-- manual-meta: {"module": "Reports", "page": "Doc Verification System (DVS)", "task": "Access DVS portal", "action": "view", "roles": [], "route": "/reports/otherReports/docVerificationSystem(DVS)", "screenshots": ["screenshots/reports/doc_verification_system_dvs.png"], "keywords": ["dvs", "verification", "document check"], "task_order": 1} -->
#### Task: Access DVS portal

**Purpose:** To verify system documentation as required by VAT regulations.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Active session with DVS permissions.

**Steps:**
1. Navigate to the Reports module.
2. Select 'Doc Verification System (DVS)' from the list.

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** The screen loads the Doc Verification System interface.

**Warnings:**
* No specific warning was identified

**Search keywords:** dvs, verification, document check

### Page: HSCode Wise Sales & VAT

![Hscode Wise Sales Vat: Screen](screenshots/reports/hscode_wise_sales_vat.png)

![Hscode Wise Sales Vat: Show](screenshots/reports/hscode_wise_sales_vat_show.png)

**Page purpose:** This report provides a breakdown of sales quantity and VAT information categorized by HS Code and item.

**Route:** `/reports/otherReports/hsCodeVatSummary`

<!-- manual-meta: {"module": "Reports", "page": "HSCode Wise Sales & VAT", "task": "Filter HSCode VAT sales summary", "action": "filter", "roles": [], "route": "/reports/otherReports/hsCodeVatSummary", "screenshots": ["screenshots/reports/hscode_wise_sales_vat.png", "screenshots/reports/hscode_wise_sales_vat_show.png"], "keywords": ["hs code", "vat", "sales summary", "item code"], "task_order": 1} -->
#### Task: Filter HSCode VAT sales summary

**Purpose:** To analyze sales performance and VAT liability per HS Code.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must be on the 'HSCode Wise Sales & Vat' page.

**Steps:**
1. Set the 'From Date' and 'To Date' range.
2. Click the 'View' button.

**Fields and controls:**
* **From Date:** Start of the sales data period.
* **To Date:** End of the sales data period.

**Expected result:** The report displays data including HS Code, Item Code, Item Name, Sales Quantity, Rate, Value, and VAT figures.

**Warnings:**
* No specific warning was identified

**Search keywords:** hs code, vat, sales summary, item code

### Page: Inventory Reconciliation

![Inventory Reconciliation: Screen](screenshots/reports/inventory_reconciliation.png)

**Page purpose:** A reporting page designed to reconcile inventory counts against records to ensure accuracy.

**Route:** `/reports/otherReports/inventoryReport`

<!-- manual-meta: {"module": "Reports", "page": "Inventory Reconciliation", "task": "Filter inventory data", "action": "filter", "roles": [], "route": "/reports/otherReports/inventoryReport", "screenshots": ["screenshots/reports/inventory_reconciliation.png"], "keywords": ["inventory", "reconciliation", "stock count"], "task_order": 1} -->
#### Task: Filter inventory data

**Purpose:** To generate an inventory reconciliation report for a specific time frame.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must have access to the Inventory Reconciliation menu.

**Steps:**
1. Select the 'View Type' from the dropdown.
2. Input the 'From Date' and 'To Date'.
3. Click the 'View' button to execute the search.

**Fields and controls:**
* **View Type:** Selector for the type of inventory view required.
* **From Date:** Beginning of the reconciliation period.
* **To Date:** Ending of the reconciliation period.

**Expected result:** Reconciliation data will be generated based on the chosen filters.

**Warnings:**
* No specific warning was identified

**Search keywords:** inventory, reconciliation, stock count

### Page: Material Issue Report

![Material Issue Report: Screen](screenshots/reports/material_issue_report.png)

**Page purpose:** This page is used to report on material issuance for production or internal consumption.

**Route:** `/reports/otherReports/materialIssueReport`

<!-- manual-meta: {"module": "Reports", "page": "Material Issue Report", "task": "Generate material issue report", "action": "view", "roles": [], "route": "/reports/otherReports/materialIssueReport", "screenshots": ["screenshots/reports/material_issue_report.png"], "keywords": ["material issue", "stock consumption", "production supply"], "task_order": 1} -->
#### Task: Generate material issue report

**Purpose:** To view records of material consumption or transfers.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to MIS reports.

**Steps:**
1. Select the 'Branch' from the dropdown.
2. Select a 'Sort By' option if required.
3. Enter the 'From Date' and 'To Date'.
4. Click 'View' to load the report.

**Fields and controls:**
* **Branch:** Select the relevant branch.
* **Sort By:** Defines the sort order of the output.
* **From Date:** Start date for material issues.
* **To Date:** End date for material issues.

**Expected result:** The report displays material issue data according to the selected branch and date range.

**Warnings:**
* No specific warning was identified

**Search keywords:** material issue, stock consumption, production supply

### Page: Mushak 9.1 (VAT Return)

![Mis Report: Screen](screenshots/reports/mis_report.png)

![Mis Report: Show](screenshots/reports/mis_report_show.png)

**Page purpose:** This page provides the official Value Added Tax (VAT) return form for submission.

**Route:** `/reports/mushakForms/mushak9.1`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 9.1 (VAT Return)", "task": "View VAT Return", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak9.1", "screenshots": ["screenshots/reports/mis_report.png", "screenshots/reports/mis_report_show.png"], "keywords": ["VAT", "Return", "Mushak 9.1"], "task_order": 1} -->
#### Task: View VAT Return

**Purpose:** To review the VAT return details for a specific month.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* A valid month and year selected.

**Steps:**
1. Select the month and year from the month field.
2. Click the View button.

**Fields and controls:**
* **mushakDate:** The target month and year for the return.

**Expected result:** The VAT return form is populated with the corresponding data.

**Warnings:**
* No specific warning was identified

**Search keywords:** VAT, Return, Mushak 9.1

### Page: Mushak 4.3 (Price Declaration)

![Mushak 4 3 Price Declaration: Screen](screenshots/reports/mushak_4_3_price_declaration.png)

**Page purpose:** This page allows users to view the price declaration details of items.

**Route:** `/reports/mushakForms/mushak4.3`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 4.3 (Price Declaration)", "task": "Search Items", "action": "search", "roles": [], "route": "/reports/mushakForms/mushak4.3", "screenshots": ["screenshots/reports/mushak_4_3_price_declaration.png"], "keywords": ["Price", "Declaration", "Mushak 4.3"], "task_order": 1} -->
#### Task: Search Items

**Purpose:** To quickly locate a specific item's price declaration.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the reports module.

**Steps:**
1. Enter the item name into the search field.
2. View the filtered result in the table.

**Fields and controls:**
* **Item Name Search:** Field to search for a specific item by name.

**Expected result:** The table updates to show items matching the search criteria.

**Warnings:**
* No specific warning was identified

**Search keywords:** Price, Declaration, Mushak 4.3

### Page: Mushak 4.4 (Item Destroy)

![Mushak 4 4 Item Destroy: Screen](screenshots/reports/mushak_4_4_item_destroy.png)

**Page purpose:** This page is used to view details of destroyed items.

**Route:** `/reports/mushakForms/mushak4.4`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 4.4 (Item Destroy)", "task": "Filter Item Destruction", "action": "filter", "roles": [], "route": "/reports/mushakForms/mushak4.4", "screenshots": ["screenshots/reports/mushak_4_4_item_destroy.png"], "keywords": ["Destroy", "Mushak 4.4"], "task_order": 1} -->
#### Task: Filter Item Destruction

**Purpose:** To view item destruction records within a specific timeframe.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Records exist for the selected period.

**Steps:**
1. Select the Branch, Item Type, and Item Name.
2. Select the From Date and To Date.
3. Click the View button.

**Fields and controls:**
* **Branch:** Select the branch for which data is required.
* **fromDate:** Start date for the report period.
* **toDate:** End date for the report period.

**Expected result:** Records matching the criteria are displayed.

**Warnings:**
* No specific warning was identified

**Search keywords:** Destroy, Mushak 4.4

### Page: Mushak 4.5 (Accident Destroy)

![Mushak 4 5 Accident Destroy: Screen](screenshots/reports/mushak_4_5_accident_destroy.png)

**Page purpose:** This page is used to view items destroyed due to accidents.

**Route:** `/reports/mushakForms/mushak4.5`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 4.5 (Accident Destroy)", "task": "Filter Accident Destruction", "action": "filter", "roles": [], "route": "/reports/mushakForms/mushak4.5", "screenshots": ["screenshots/reports/mushak_4_5_accident_destroy.png"], "keywords": ["Accident", "Destroy", "Mushak 4.5"], "task_order": 1} -->
#### Task: Filter Accident Destruction

**Purpose:** To view records of items lost due to accidents.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Relevant accident destruction logs exist.

**Steps:**
1. Select the Branch, Item Type, and Item Name.
2. Select the date range using From Date and To Date.
3. Click the View button.

**Fields and controls:**
* **fromDate:** The beginning date of the range.
* **toDate:** The end date of the range.

**Expected result:** The relevant accident destruction data is populated.

**Warnings:**
* No specific warning was identified

**Search keywords:** Accident, Destroy, Mushak 4.5

### Page: Mushak 4.6 (Waste Disposal)

![Mushak 4 6 Waste Disposal: Screen](screenshots/reports/mushak_4_6_waste_disposal.png)

**Page purpose:** This page provides an overview of waste disposal records.

**Route:** `/reports/mushakForms/mushak4.6`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 4.6 (Waste Disposal)", "task": "View Waste Disposal Logs", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak4.6", "screenshots": ["screenshots/reports/mushak_4_6_waste_disposal.png"], "keywords": ["Waste", "Disposal", "Mushak 4.6"], "task_order": 1} -->
#### Task: View Waste Disposal Logs

**Purpose:** To review historical waste disposal data.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Waste records have been previously logged.

**Steps:**
1. Navigate to the report page.
2. Review the generated table list.

**Fields and controls:**
* **rows per page:** Configures how many records show per page.

**Expected result:** The table shows the list of waste disposal events.

**Warnings:**
* No specific warning was identified

**Search keywords:** Waste, Disposal, Mushak 4.6

### Page: Mushak 6.10 (P&S +2 Lakh)

![Mushak 6 10 P S 2 Lakh: Screen](screenshots/reports/mushak_6_10_p_s_2_lakh.png)

![Mushak 6 10 P S 2 Lakh: Show](screenshots/reports/mushak_6_10_p_s_2_lakh_show.png)

**Page purpose:** This report summarizes purchases and sales over two lakh.

**Route:** `/reports/mushakForms/mushak6.10`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.10 (P&S +2 Lakh)", "task": "Generate P&S Report", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak6.10", "screenshots": ["screenshots/reports/mushak_6_10_p_s_2_lakh.png", "screenshots/reports/mushak_6_10_p_s_2_lakh_show.png"], "keywords": ["P&S", "2 Lakh", "Mushak 6.10"], "task_order": 1} -->
#### Task: Generate P&S Report

**Purpose:** To generate a report for large purchase and sales transactions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* A valid date range is selected.

**Steps:**
1. Select the Branch.
2. Pick the From Date and To Date.
3. Click the View button.

**Fields and controls:**
* **Branch:** Select the branch.

**Expected result:** Report data is populated. If not available, an error or notification will appear.

**Warnings:**
* No specific warning was identified

**Search keywords:** P&S, 2 Lakh, Mushak 6.10

### Page: Mushak 6.1 (Purchase Register)

![Mushak 6 1 Purchase Register: Screen](screenshots/reports/mushak_6_1_purchase_register.png)

**Page purpose:** This page displays the purchase register reports.

**Route:** `/reports/mushakForms/mushak6.1`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.1 (Purchase Register)", "task": "Filter Purchase Register", "action": "filter", "roles": [], "route": "/reports/mushakForms/mushak6.1", "screenshots": ["screenshots/reports/mushak_6_1_purchase_register.png"], "keywords": ["Purchase", "Register", "Mushak 6.1"], "task_order": 1} -->
#### Task: Filter Purchase Register

**Purpose:** To narrow down the purchase register data by date and type.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Available purchase data.

**Steps:**
1. Select Item Type and Branch.
2. Select From Date and To Date.
3. Select the display format (Bangla or English).
4. Click the View button.

**Fields and controls:**
* **Bangla format:** Display the report in Bengali.
* **English format:** Display the report in English.

**Expected result:** The purchase register is filtered according to the selected format and date range.

**Warnings:**
* No specific warning was identified

**Search keywords:** Purchase, Register, Mushak 6.1

### Page: Mushak 6.2.1 (P&S Register)

![Mushak 6 2 1 P S Register: Screen](screenshots/reports/mushak_6_2_1_p_s_register.png)

**Page purpose:** This page allows users to view the Purchases and Sales register.

**Route:** `/reports/mushakForms/mushak6-2-1`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.2.1 (P&S Register)", "task": "Generate P&S Register", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak6-2-1", "screenshots": ["screenshots/reports/mushak_6_2_1_p_s_register.png"], "keywords": ["P&S", "Register", "Mushak 6.2.1"], "task_order": 1} -->
#### Task: Generate P&S Register

**Purpose:** To generate a comprehensive report of purchases and sales.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* A date range has been specified.

**Steps:**
1. Select the Item Type, Branch, and Item Name.
2. Select the report date range.
3. Click the View button.

**Fields and controls:**
* **Item Type:** Type of item.

**Expected result:** The P&S register for the selected item and time period is displayed.

**Warnings:**
* No specific warning was identified

**Search keywords:** P&S, Register, Mushak 6.2.1

### Page: Mushak 6.2 (Sales Register)

![Mushak 6 2 Sales Register: Screen](screenshots/reports/mushak_6_2_sales_register.png)

**Page purpose:** This page provides a report of sales records based on user-selected criteria.

**Route:** `/reports/mushakForms/mushak6.2`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.2 (Sales Register)", "task": "Filter and View Sales Register", "action": "filter", "roles": [], "route": "/reports/mushakForms/mushak6.2", "screenshots": ["screenshots/reports/mushak_6_2_sales_register.png"], "keywords": ["Sales report", "Sales Register", "Mushak 6.2"], "task_order": 1} -->
#### Task: Filter and View Sales Register

**Purpose:** To view a specific sales register report based on item type, branch, and date range.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Data must exist for the selected criteria.

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.2 (Sales Register).
2. Select an Item Type from the dropdown.
3. Select a Branch.
4. Choose a From Date and To Date using the date picker.
5. Select a report format (Bangla or English).
6. Click the View button to display the report.

**Fields and controls:**
* **Item Type:** Dropdown to select the category of sales items.
* **Item:** Dropdown to specify the particular item name.
* **Branch:** Dropdown to select the relevant branch.
* **From Date:** The start date for the sales report.
* **To Date:** The end date for the sales report.

**Expected result:** A list of sales records corresponding to the selected filters, or a message stating 'Sales information not available'.

**Warnings:**
* If no records are found for the selected criteria, the system will display a notification message.

**Search keywords:** Sales report, Sales Register, Mushak 6.2

### Page: Mushak 6.3 (Sales Invoice)

![Mushak 6 3 Sales Invoice: Screen](screenshots/reports/mushak_6_3_sales_invoice.png)

![Mushak 6 3 Sales Invoice: Show](screenshots/reports/mushak_6_3_sales_invoice_show.png)

**Page purpose:** This page allows users to search and view sales invoice records.

**Route:** `/reports/mushakForms/mushak6.3`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.3 (Sales Invoice)", "task": "Search Sales Invoices", "action": "search", "roles": [], "route": "/reports/mushakForms/mushak6.3", "screenshots": ["screenshots/reports/mushak_6_3_sales_invoice.png", "screenshots/reports/mushak_6_3_sales_invoice_show.png"], "keywords": ["Sales Invoice", "Invoice report", "Mushak 6.3"], "task_order": 1} -->
#### Task: Search Sales Invoices

**Purpose:** To find specific sales invoices for reporting or verification.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Invoices must be generated in the system.

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.3 (Sales Invoice).
2. Select the Branch from the dropdown.
3. Set the From Date and To Date range.
4. Click the View button to generate the list.
5. Use the 'BOE, BIN, Inv No Search' field to narrow results if necessary.

**Fields and controls:**
* **Select Branch:** Dropdown to select the business branch.
* **BOE, BIN, Inv No Search:** Search input for filtering invoices by bill of entry, business identification number, or invoice number.

**Expected result:** A table populated with relevant sales invoices.

**Warnings:**
* No specific warning was identified

**Search keywords:** Sales Invoice, Invoice report, Mushak 6.3

### Page: Mushak 6.4 (Issue MFG.)

![Mushak 6 4 Issue Mfg: Screen](screenshots/reports/mushak_6_4_issue_mfg.png)

![Mushak 6 4 Issue Mfg: Show](screenshots/reports/mushak_6_4_issue_mfg_show.png)

**Page purpose:** Provides reports for contract manufacturing issue and receive transactions.

**Route:** `/reports/mushakForms/mushak6.4`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.4 (Issue MFG.)", "task": "View Contract Manufacturing Reports", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak6.4", "screenshots": ["screenshots/reports/mushak_6_4_issue_mfg.png", "screenshots/reports/mushak_6_4_issue_mfg_show.png"], "keywords": ["Manufacturing report", "Issue MFG", "Contract manufacturing"], "task_order": 1} -->
#### Task: View Contract Manufacturing Reports

**Purpose:** To report on raw materials issued or received for contract manufacturing.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Contract manufacturing transactions must have occurred.

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.4 (Issue MFG.).
2. Toggle between the 'CONTRACT MANUFACTURING ISSUE' or 'CONTRACT MANUFACTURING RECEIVE' tabs.
3. Select the Branch, From Date, To Date, and Issue Type.
4. Click the View button.

**Fields and controls:**
* **Branch:** Select the relevant branch.
* **Issue Type:** Dropdown to define the type of issuance or receipt.

**Expected result:** A table showing transaction details like Challan No, Supplier, Date, and Quantity.

**Warnings:**
* No specific warning was identified

**Search keywords:** Manufacturing report, Issue MFG, Contract manufacturing

### Page: Mushak 6.5 (Stock Transfer)

![Mushak 6 5 Stock Transfer: Screen](screenshots/reports/mushak_6_5_stock_transfer.png)

![Mushak 6 5 Stock Transfer: Show](screenshots/reports/mushak_6_5_stock_transfer_show.png)

**Page purpose:** Used to monitor records of stock transfers between branches or locations.

**Route:** `/reports/mushakForms/mushak6.5`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.5 (Stock Transfer)", "task": "Browse Stock Transfers", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak6.5", "screenshots": ["screenshots/reports/mushak_6_5_stock_transfer.png", "screenshots/reports/mushak_6_5_stock_transfer_show.png"], "keywords": ["Stock transfer report", "Inventory movement"], "task_order": 1} -->
#### Task: Browse Stock Transfers

**Purpose:** To verify the history of stock movements.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Stock transfer transactions must be recorded.

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.5 (Stock Transfer).
2. Select the Branch Name and Item Type.
3. Click the View button to load the transfer records.
4. Use the 'Transfer No Search' field to filter the table list.

**Fields and controls:**
* **Transfer No Search:** Filter table by transfer identification number.

**Expected result:** A list of stock transfers with details such as Transfer No, Branch, and Quantity.

**Warnings:**
* No specific warning was identified

**Search keywords:** Stock transfer report, Inventory movement

### Page: Mushak 6.6 (VDS Certificate)

![Mushak 6 6 Vds Certificate: Screen](screenshots/reports/mushak_6_6_vds_certificate.png)

![Mushak 6 6 Vds Certificate: Show](screenshots/reports/mushak_6_6_vds_certificate_show.png)

**Page purpose:** Used for reviewing VAT Deducted at Source (VDS) certificates.

**Route:** `/reports/mushakForms/mushak6.6`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.6 (VDS Certificate)", "task": "Review VDS Certificates", "action": "filter", "roles": [], "route": "/reports/mushakForms/mushak6.6", "screenshots": ["screenshots/reports/mushak_6_6_vds_certificate.png", "screenshots/reports/mushak_6_6_vds_certificate_show.png"], "keywords": ["VDS", "VAT Deducted at Source", "Certificate report"], "task_order": 1} -->
#### Task: Review VDS Certificates

**Purpose:** To audit and view the status of VDS certificates.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* VDS entries must exist in the system.

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.6 (VDS Certificate).
2. Select the Report Type (e.g., VDS Certificate Issue) and the Branch.
3. Enter the date range.
4. Select a status filter: All, Pending, or Complete.
5. Click the View button.

**Fields and controls:**
* **Select Report Type:** Dropdown to select certificate type.
* **Status Filter:** Radio buttons to filter by certificate completion status (All, Pending, Complete).

**Expected result:** Table showing certificates including Certificate No, Chalan No, and Deducted Amount.

**Warnings:**
* No specific warning was identified

**Search keywords:** VDS, VAT Deducted at Source, Certificate report

### Page: Mushak 6.7 (Credit Note)

![Mushak 6 7 Credit Note: Screen](screenshots/reports/mushak_6_7_credit_note.png)

**Page purpose:** Provides a report of issued credit notes.

**Route:** `/reports/mushakForms/mushak6.7`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.7 (Credit Note)", "task": "Search Credit Notes", "action": "search", "roles": [], "route": "/reports/mushakForms/mushak6.7", "screenshots": ["screenshots/reports/mushak_6_7_credit_note.png"], "keywords": ["Credit Note", "Return report"], "task_order": 1} -->
#### Task: Search Credit Notes

**Purpose:** To find and review specific credit notes.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Credit notes must have been created.

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.7 (Credit Note).
2. Select Branch and Date range.
3. Use the 'Sales Invoice Search' box to find related notes.
4. Click View.

**Fields and controls:**
* **Sales Invoice Search:** Search input for credit notes related to specific sales invoices.

**Expected result:** A table populated with credit note details.

**Warnings:**
* No specific warning was identified

**Search keywords:** Credit Note, Return report

### Page: Mushak 6.8 (Debit Note)

![Mushak 6 8 Debit Note: Screen](screenshots/reports/mushak_6_8_debit_note.png)

![Mushak 6 8 Debit Note: Show](screenshots/reports/mushak_6_8_debit_note_show.png)

**Page purpose:** Provides a report of issued debit notes.

**Route:** `/reports/mushakForms/mushak6.8`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 6.8 (Debit Note)", "task": "Search Debit Notes", "action": "search", "roles": [], "route": "/reports/mushakForms/mushak6.8", "screenshots": ["screenshots/reports/mushak_6_8_debit_note.png", "screenshots/reports/mushak_6_8_debit_note_show.png"], "keywords": ["Debit Note"], "task_order": 1} -->
#### Task: Search Debit Notes

**Purpose:** To find and review specific debit notes.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Debit notes must have been created.

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 6.8 (Debit Note).
2. Select the Branch Name, Form Date, and To Date.
3. Use the 'Purchase Invoice Search' to find related notes.
4. Click View.

**Fields and controls:**
* **Purchase Invoice Search:** Search input for debit notes related to specific purchase invoices.

**Expected result:** A table populated with debit note details.

**Warnings:**
* No specific warning was identified

**Search keywords:** Debit Note

### Page: Mushak 9.1 (VAT Return)

![Mushak 9 1 Vat Return: Screen](screenshots/reports/mushak_9_1_vat_return.png)

![Mushak 9 1 Vat Return: Show](screenshots/reports/mushak_9_1_vat_return_show.png)

**Page purpose:** Used to generate, view, and print the official VAT Return form.

**Route:** `/reports/mushakForms/mushak9.1`

<!-- manual-meta: {"module": "Reports", "page": "Mushak 9.1 (VAT Return)", "task": "Generate VAT Return", "action": "view", "roles": [], "route": "/reports/mushakForms/mushak9.1", "screenshots": ["screenshots/reports/mushak_9_1_vat_return.png", "screenshots/reports/mushak_9_1_vat_return_show.png"], "keywords": ["VAT Return", "Mushak 9.1", "Tax return"], "task_order": 1} -->
#### Task: Generate VAT Return

**Purpose:** To view the VAT return details for a selected month.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Transactions for the period must be recorded and posted.

**Steps:**
1. Navigate to Reports > Mushak Forms > Mushak 9.1 (VAT Return).
2. Select the Month/Year in the 'Year And Month' field.
3. Click the View button to display the form.
4. Click the Print button to output the form, or Posting to commit the return.

**Fields and controls:**
* **Year And Month:** Select the period for the VAT return.

**Expected result:** The VAT return form is populated with the financial summary for the selected period.

**Warnings:**
* No specific warning was identified

**Search keywords:** VAT Return, Mushak 9.1, Tax return

### Page: Mushak Forms

![Mushak Forms: Screen](screenshots/reports/mushak_forms.png)

![Mushak Forms: Show](screenshots/reports/mushak_forms_show.png)

**Page purpose:** This page provides access to various government-mandated VAT forms and registers for record-keeping and compliance reporting.

**Route:** `/reports/mushakForms`

<!-- manual-meta: {"module": "Reports", "page": "Mushak Forms", "task": "View Mushak Report", "action": "view", "roles": [], "route": "/reports/mushakForms", "screenshots": ["screenshots/reports/mushak_forms.png", "screenshots/reports/mushak_forms_show.png"], "keywords": ["Mushak", "VAT form", "register", "compliance report"], "task_order": 1} -->
#### Task: View Mushak Report

**Purpose:** To generate and view specific VAT-related reports like purchase or sales registers.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must have navigation access to Reports

**Steps:**
1. Navigate to the Reports module
2. Click on 'Mushak Forms' to expand the list
3. Select the desired Mushak form (e.g., Mushak 6.2 Sales Register)
4. Select the branch and date range as required
5. Click the 'View' button

**Fields and controls:**
* **Select Branch:** Dropdown to select the company branch.
* **Enter From Date:** Date picker for the start of the report range.
* **Enter To Date:** Date picker for the end of the report range.

**Expected result:** A table populated with relevant record data based on the chosen filters.

**Warnings:**
* No specific warning was identified

**Search keywords:** Mushak, VAT form, register, compliance report

### Page: Partner Vs Stock Report

![Partner Vs Stock: Screen](screenshots/reports/partner_vs_stock.png)

**Page purpose:** This report displays a comparison of stock levels relative to partners/customers.

**Route:** `/reports/otherReports/partnerVsStock`

<!-- manual-meta: {"module": "Reports", "page": "Partner Vs Stock Report", "task": "View Partner Vs Stock Report", "action": "view", "roles": [], "route": "/reports/otherReports/partnerVsStock", "screenshots": ["screenshots/reports/partner_vs_stock.png"], "keywords": ["stock report", "partner inventory", "stock analysis"], "task_order": 1} -->
#### Task: View Partner Vs Stock Report

**Purpose:** To analyze stock inventory details associated with specific partners.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Active session in Prime VAT

**Steps:**
1. Navigate to Reports > MIS Report
2. Select 'Partner Vs Stock' from the left sidebar
3. Choose a branch, customer name, and item filter
4. Click the 'View' button

**Fields and controls:**
* **Branch:** Select the company branch.
* **Customer Name:** Field to filter by a specific customer.
* **Item:** Dropdown to select a specific stock item.

**Expected result:** The grid populates with item names, codes, units of measurement, price, and current stock status.

**Warnings:**
* No specific warning was identified

**Search keywords:** stock report, partner inventory, stock analysis

### Page: Payment Method Wise Report

![Payment Method Wise Report: Screen](screenshots/reports/payment_method_wise_report.png)

![Payment Method Wise Report: Show](screenshots/reports/payment_method_wise_report_show.png)

**Page purpose:** Displays financial reports categorized by the payment methods used for transactions.

**Route:** `/reports/otherReports/paymentMethodWiseReport`

<!-- manual-meta: {"module": "Reports", "page": "Payment Method Wise Report", "task": "View Payment Method Wise Report", "action": "view", "roles": [], "route": "/reports/otherReports/paymentMethodWiseReport", "screenshots": ["screenshots/reports/payment_method_wise_report.png", "screenshots/reports/payment_method_wise_report_show.png"], "keywords": ["payment summary", "transaction audit", "financial report"], "task_order": 1} -->
#### Task: View Payment Method Wise Report

**Purpose:** To audit and view transaction summaries based on the payment method (e.g., cash, credit, bank transfer).

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to MIS reports

**Steps:**
1. Navigate to Reports > MIS Report
2. Select 'Payment Method Wise Report'
3. Specify Item Type, Payment Method Type, and date range
4. Click the 'View' button

**Fields and controls:**
* **Item Type:** Category of items for the report (e.g., Sales).
* **Payment Method Type:** Filter by payment method or 'All'.

**Expected result:** A data view displaying transactions grouped by payment method.

**Warnings:**
* No specific warning was identified

**Search keywords:** payment summary, transaction audit, financial report

### Page: Production Report

![Production Report: Screen](screenshots/reports/production_report.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/reports/otherReports/productionReport`

<!-- manual-meta: {"module": "Reports", "page": "Production Report", "task": "Use Production Report", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/reports/otherReports/productionReport", "screenshots": ["screenshots/reports/production_report.png"], "keywords": ["Production Report", "production report"], "task_order": 1} -->
#### Task: Use Production Report

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the Production Report page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* **From Date:** Visible date control.
* **To Date:** Visible date control.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** Production Report, production report

### Page: Purchase Report

![Purchase Report: Screen](screenshots/reports/purchase_report.png)

![Purchase Report: Show](screenshots/reports/purchase_report_show.png)

**Page purpose:** Generates a detailed report of all procurement and purchase transactions.

**Route:** `/reports/otherReports/purchaseReport`

<!-- manual-meta: {"module": "Reports", "page": "Purchase Report", "task": "View Purchase Report", "action": "view", "roles": [], "route": "/reports/otherReports/purchaseReport", "screenshots": ["screenshots/reports/purchase_report.png", "screenshots/reports/purchase_report_show.png"], "keywords": ["procurement", "purchase audit", "vendor report"], "task_order": 1} -->
#### Task: View Purchase Report

**Purpose:** To review purchase transaction logs over a specified time period.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Procurement data must exist in the system

**Steps:**
1. Navigate to Reports > MIS Report
2. Select 'Purchase Report'
3. Set the Branch, Sort By, and date range filters
4. Click 'View'

**Fields and controls:**
* **Branch:** Filter for the organizational branch.
* **Sort By:** Defines the sort order of the resulting report.

**Expected result:** A list of purchase transactions matching the applied filters.

**Warnings:**
* No specific warning was identified

**Search keywords:** procurement, purchase audit, vendor report

### Page: Purchase Report by Category

![Purchase Report By Category: Screen](screenshots/reports/purchase_report_by_category.png)

![Purchase Report By Category: Show](screenshots/reports/purchase_report_by_category_show.png)

**Page purpose:** Provides purchase transaction information organized by item categories.

**Route:** `/reports/otherReports/purchaseReportByCategory`

<!-- manual-meta: {"module": "Reports", "page": "Purchase Report by Category", "task": "View Category-wise Purchase Report", "action": "view", "roles": [], "route": "/reports/otherReports/purchaseReportByCategory", "screenshots": ["screenshots/reports/purchase_report_by_category.png", "screenshots/reports/purchase_report_by_category_show.png"], "keywords": ["categorized purchase", "item classification", "procurement summary"], "task_order": 1} -->
#### Task: View Category-wise Purchase Report

**Purpose:** To analyze purchase volumes categorized by item groupings.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Items must be assigned to categories

**Steps:**
1. Navigate to Reports > MIS Report
2. Select 'Purchase Report by Category'
3. Select the desired date range
4. Click 'View'

**Fields and controls:**
* **Enter From Date:** Start date for report extraction.
* **Enter To Date:** End date for report extraction.

**Expected result:** Categorized purchase transaction summaries appear on the screen.

**Warnings:**
* No specific warning was identified

**Search keywords:** categorized purchase, item classification, procurement summary

### Page: Purchase/Sales Details

![Purchase Sales Details: Screen](screenshots/reports/purchase_sales_details.png)

**Page purpose:** Offers a comprehensive view of both purchase and sales transaction details.

**Route:** `/reports/otherReports/purchaseSalesDetails`

<!-- manual-meta: {"module": "Reports", "page": "Purchase/Sales Details", "task": "View Purchase and Sales Details", "action": "view", "roles": [], "route": "/reports/otherReports/purchaseSalesDetails", "screenshots": ["screenshots/reports/purchase_sales_details.png"], "keywords": ["transaction log", "audit", "detailed report"], "task_order": 1} -->
#### Task: View Purchase and Sales Details

**Purpose:** To view granular data for both sales and purchase operations in one report.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* System must contain both sales and purchase data

**Steps:**
1. Navigate to Reports > MIS Report
2. Select 'Purchase/Sales Details'
3. Choose date range and record type (Purchase or Sales)
4. Click 'View'

**Fields and controls:**
* **Select Type:** Toggle between Purchase or Sales view.

**Expected result:** A detailed table of transactions based on the selected type.

**Warnings:**
* No specific warning was identified

**Search keywords:** transaction log, audit, detailed report

### Page: Wastage Sales

![Reports: Screen](screenshots/reports/reports.png)

![Reports: Show](screenshots/reports/reports_show.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/reports`

<!-- manual-meta: {"module": "Reports", "page": "Wastage Sales", "task": "Use Wastage Sales", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/reports", "screenshots": ["screenshots/reports/reports.png", "screenshots/reports/reports_show.png"], "keywords": ["Wastage Sales", "reports"], "task_order": 1} -->
#### Task: Use Wastage Sales

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the Wastage Sales page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* **From Date:** Visible date control.
* **To Date:** Visible date control.
* **BOE, BIN, Inv No Search:** Visible text control.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** Wastage Sales, reports

### Page: Sales & Purchase Compare

![Sales Purchase Compare: Screen](screenshots/reports/sales_purchase_compare.png)

![Sales Purchase Compare: Show](screenshots/reports/sales_purchase_compare_show.png)

**Page purpose:** This page provides a comparison between sales and purchase data to analyze trends or discrepancies over specific dates.

**Route:** `/reports/otherReports/salesAndPurchaseCompare`

<!-- manual-meta: {"module": "Reports", "page": "Sales & Purchase Compare", "task": "View Sales & Purchase Comparison", "action": "view", "roles": [], "route": "/reports/otherReports/salesAndPurchaseCompare", "screenshots": ["screenshots/reports/sales_purchase_compare.png", "screenshots/reports/sales_purchase_compare_show.png"], "keywords": ["comparison", "sales vs purchase", "report", "analysis"], "task_order": 1} -->
#### Task: View Sales & Purchase Comparison

**Purpose:** To compare the sales and purchase data between two selected dates.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Data must be available for the selected dates.

**Steps:**
1. Navigate to Reports > MIS Report > Sales & Purchase Compare.
2. Select the Branch from the dropdown.
3. Select the Type.
4. Select the Based On frequency (e.g., Day).
5. Select the Purchase Compare (Date).
6. Select the Sales Compare (Date).
7. Click the View button.

**Fields and controls:**
* **Branch:** Dropdown to select the relevant branch.
* **Type:** Dropdown for report type selection.
* **Based On:** Dropdown for time frequency selection.
* **Purchase Compare (Date):** Date picker for the purchase data start point.
* **Sales Compare (Date):** Date picker for the sales data comparison point.

**Expected result:** The system displays a table comparing Amount, VAT, and Grand Total for both Purchase and Sales criteria.

**Warnings:**
* If no data exists for the selected dates, a 'No data found' message will appear.

**Search keywords:** comparison, sales vs purchase, report, analysis

### Page: Sales Report

![Sales Report: Screen](screenshots/reports/sales_report.png)

**Page purpose:** This page provides a detailed report of sales transactions within a specific date range.

**Route:** `/reports/otherReports/salesReport`

<!-- manual-meta: {"module": "Reports", "page": "Sales Report", "task": "Generate Sales Report", "action": "view", "roles": [], "route": "/reports/otherReports/salesReport", "screenshots": ["screenshots/reports/sales_report.png"], "keywords": ["sales", "invoices", "transactions", "report"], "task_order": 1} -->
#### Task: Generate Sales Report

**Purpose:** To view a summary or detailed list of sales transactions for a chosen period.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Sales Report.
2. Select the Branch.
3. Select the sorting preference in 'Sort By'.
4. Pick the 'From Date'.
5. Pick the 'To Date'.
6. Click the View button.

**Fields and controls:**
* **Branch:** Dropdown to select the branch.
* **Sort By:** Criteria to sort the report data.
* **From Date:** Starting date for the report range.
* **To Date:** Ending date for the report range.

**Expected result:** A list of sales transactions matching the specified criteria is displayed.

**Warnings:**
* No specific warning was identified

**Search keywords:** sales, invoices, transactions, report

### Page: Sales Report by Category

![Sales Report By Category: Screen](screenshots/reports/sales_report_by_category.png)

![Sales Report By Category: Show](screenshots/reports/sales_report_by_category_show.png)

**Page purpose:** This page displays sales data filtered by product categories for a specific date range.

**Route:** `/reports/otherReports/salesReportByCategory`

<!-- manual-meta: {"module": "Reports", "page": "Sales Report by Category", "task": "View Category-Wise Sales", "action": "view", "roles": [], "route": "/reports/otherReports/salesReportByCategory", "screenshots": ["screenshots/reports/sales_report_by_category.png", "screenshots/reports/sales_report_by_category_show.png"], "keywords": ["sales report", "category", "product group"], "task_order": 1} -->
#### Task: View Category-Wise Sales

**Purpose:** To analyze sales performance categorized by product groups.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Sales Report by Category.
2. Select the 'Enter From Date'.
3. Select the 'Enter To Date'.
4. Click the View button.

**Fields and controls:**
* **Enter From Date:** The start date for the sales category report.
* **Enter To Date:** The end date for the sales category report.

**Expected result:** Displays a breakdown of sales figures organized by category for the selected date range.

**Warnings:**
* No specific warning was identified

**Search keywords:** sales report, category, product group

### Page: Sales & Stock Summary

![Sales Stock Summary: Screen](screenshots/reports/sales_stock_summary.png)

![Sales Stock Summary: Show](screenshots/reports/sales_stock_summary_show.png)

**Page purpose:** This page generates a combined summary report showing sales performance against current stock levels for a selected month.

**Route:** `/reports/otherReports/SalesStockSummary`

<!-- manual-meta: {"module": "Reports", "page": "Sales & Stock Summary", "task": "View Sales and Stock Summary", "action": "view", "roles": [], "route": "/reports/otherReports/SalesStockSummary", "screenshots": ["screenshots/reports/sales_stock_summary.png", "screenshots/reports/sales_stock_summary_show.png"], "keywords": ["stock summary", "inventory", "sales", "monthly report"], "task_order": 1} -->
#### Task: View Sales and Stock Summary

**Purpose:** To view the correlation between purchase, sales, and closing stock for a specific month.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Sales & Stock Summary.
2. Select the Month and Year.
3. Click the View button.

**Fields and controls:**
* **Month:** The target month and year for the summary report.

**Expected result:** The system populates a report table with columns including Opening QTY, Purchase/Sales Info, and Closing Stock.

**Warnings:**
* No specific warning was identified

**Search keywords:** stock summary, inventory, sales, monthly report

### Page: Sales Summary Report

![Sales Summary Report: Screen](screenshots/reports/sales_summary_report.png)

![Sales Summary Report: Show](screenshots/reports/sales_summary_report_show.png)

**Page purpose:** A high-level overview of sales summaries based on branch and date range.

**Route:** `/reports/otherReports/salesSummaryReport`

<!-- manual-meta: {"module": "Reports", "page": "Sales Summary Report", "task": "Generate Sales Summary Report", "action": "view", "roles": [], "route": "/reports/otherReports/salesSummaryReport", "screenshots": ["screenshots/reports/sales_summary_report.png", "screenshots/reports/sales_summary_report_show.png"], "keywords": ["summary", "invoice list", "sales"], "task_order": 1} -->
#### Task: Generate Sales Summary Report

**Purpose:** To generate an invoice-level summary of sales transactions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Sales Summary Report.
2. Select the branch from 'Select Branch'.
3. Select the 'Enter From Date'.
4. Select the 'Enter To Date'.
5. Click the View button.

**Fields and controls:**
* **Select Branch:** Dropdown to select the branch.
* **Enter From Date:** Start date for the summary range.
* **Enter To Date:** End date for the summary range.

**Expected result:** A table summarizing Sales Inv No, Trade Type, Customer Name, and other transaction details.

**Warnings:**
* No specific warning was identified

**Search keywords:** summary, invoice list, sales

### Page: Stock Reconcile Report

![Stock Reconsile Report: Screen](screenshots/reports/stock_reconsile_report.png)

**Page purpose:** This page is used for reconciling stock discrepancies.

**Route:** `/reports/otherReports/stockReconsileReport`

<!-- manual-meta: {"module": "Reports", "page": "Stock Reconcile Report", "task": "View Stock Reconcile Report", "action": "view", "roles": [], "route": "/reports/otherReports/stockReconsileReport", "screenshots": ["screenshots/reports/stock_reconsile_report.png"], "keywords": ["reconcile", "stock", "audit"], "task_order": 1} -->
#### Task: View Stock Reconcile Report

**Purpose:** To check for differences between recorded and actual stock levels.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Stock Reconsile Report.
2. Select the Branch.
3. Select the From Date.
4. Click the View button.

**Fields and controls:**
* **Branch:** Select the branch for reconciliation.
* **From Date:** Date to begin reconciliation check.

**Expected result:** System populates the reconciliation findings.

**Warnings:**
* No specific warning was identified

**Search keywords:** reconcile, stock, audit

### Page: Stock Register

![Stock Register: Screen](screenshots/reports/stock_register.png)

![Stock Register: Show](screenshots/reports/stock_register_show.png)

**Page purpose:** Provides a full record of all stock movements, including opening, receipt, and issue quantities.

**Route:** `/reports/otherReports/stockRegister`

<!-- manual-meta: {"module": "Reports", "page": "Stock Register", "task": "Generate Stock Register", "action": "view", "roles": [], "route": "/reports/otherReports/stockRegister", "screenshots": ["screenshots/reports/stock_register.png", "screenshots/reports/stock_register_show.png"], "keywords": ["register", "inventory", "stock level", "closing balance"], "task_order": 1} -->
#### Task: Generate Stock Register

**Purpose:** To view current and historical stock balances and closing values.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Stock Register.
2. Select the Branch.
3. Select the Item Type.
4. Enter From Date.
5. Enter To Date.
6. Click the View button.

**Fields and controls:**
* **Select Branch:** Dropdown for branch selection.
* **Item Type:** Select category of items.
* **Negative Stock:** Checkbox to filter for items with negative quantities.

**Expected result:** A detailed table showing opening, received, issued, and closing quantities/values for items.

**Warnings:**
* No specific warning was identified

**Search keywords:** register, inventory, stock level, closing balance

<!-- manual-meta: {"module": "Reports", "page": "Stock Register", "task": "Export Stock Register", "action": "export", "roles": [], "route": "/reports/otherReports/stockRegister", "screenshots": ["screenshots/reports/stock_register.png", "screenshots/reports/stock_register_show.png"], "keywords": ["download", "export", "spreadsheet"], "task_order": 2} -->
#### Task: Export Stock Register

**Purpose:** To export stock data to a spreadsheet format.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Data must be populated in the view.

**Steps:**
1. Perform the view generation steps.
2. Click the Excel Download button.

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** A file is downloaded to the local device containing the current stock register report.

**Warnings:**
* No specific warning was identified

**Search keywords:** download, export, spreadsheet

### Page: Transaction Log

![Transaction Log: Screen](screenshots/reports/transaction_log.png)

**Page purpose:** Displays logs of system transactions for auditing purposes.

**Route:** `/reports/otherReports/auditLog`

<!-- manual-meta: {"module": "Reports", "page": "Transaction Log", "task": "View Transaction Logs", "action": "view", "roles": [], "route": "/reports/otherReports/auditLog", "screenshots": ["screenshots/reports/transaction_log.png"], "keywords": ["audit log", "history", "tracking"], "task_order": 1} -->
#### Task: View Transaction Logs

**Purpose:** To review historical transaction activity in the system.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Navigate to Reports > MIS Report > Transaction Log.
2. Select the View Type.
3. Select From Date.
4. Select To Date.
5. Click the View button.

**Fields and controls:**
* **View Type:** Select the category of log to view.
* **From Date:** Starting date for the logs.
* **To Date:** Ending date for the logs.

**Expected result:** System displays a list of transactions matching the date and type criteria.

**Warnings:**
* No specific warning was identified

**Search keywords:** audit log, history, tracking

### Page: Transit Report

![Transit Report: Screen](screenshots/reports/transit_report.png)

![Transit Report: Show](screenshots/reports/transit_report_show.png)

**Page purpose:** This page provides a report on items currently in transit, including transfer details between branches.

**Route:** `/reports/otherReports/transitReport`

<!-- manual-meta: {"module": "Reports", "page": "Transit Report", "task": "View Transit Report", "action": "view", "roles": [], "route": "/reports/otherReports/transitReport", "screenshots": ["screenshots/reports/transit_report.png", "screenshots/reports/transit_report_show.png"], "keywords": ["transfer", "stock movement", "transit", "branch transfer"], "task_order": 1} -->
#### Task: View Transit Report

**Purpose:** To monitor and review stock movement between different branches.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Reports module
* Data availability for the selected branch and date range

**Steps:**
1. Navigate to the Reports menu in the left sidebar.
2. Select 'Transit Report' from the MIS Report list.
3. Select the 'Branch' from the dropdown menu.
4. Select the 'Item Type' from the dropdown menu.
5. Enter the 'From Date' and 'To Date' in the respective date fields.
6. Click the 'View' button.

**Fields and controls:**
* **Branch:** Select the source or target branch for the report.
* **Item Type:** The category or type of items to be reported.
* **From Date:** The start date for the transit report period.
* **To Date:** The end date for the transit report period.

**Expected result:** The system displays a table containing transfer details such as Branch Name, Transfer Date, Transfer No, Qty information, and Narration, or an 'Data Not Found' message if no records exist.

**Warnings:**
* If no matching data is found for the selected criteria, a 'Data Not Found' message will appear.

**Search keywords:** transfer, stock movement, transit, branch transfer

### Page: Treasury Deposit Report

![Treasury Deposit Report: Screen](screenshots/reports/treasury_deposit_report.png)

![Treasury Deposit Report: Show](screenshots/reports/treasury_deposit_report_show.png)

**Page purpose:** This page provides a consolidated report of treasury deposits within a specified timeframe.

**Route:** `/reports/otherReports/treasuryDepositReport`

<!-- manual-meta: {"module": "Reports", "page": "Treasury Deposit Report", "task": "View Treasury Deposit Report", "action": "view", "roles": [], "route": "/reports/otherReports/treasuryDepositReport", "screenshots": ["screenshots/reports/treasury_deposit_report.png", "screenshots/reports/treasury_deposit_report_show.png"], "keywords": ["deposit", "treasury", "bank deposit"], "task_order": 1} -->
#### Task: View Treasury Deposit Report

**Purpose:** To view and verify records of deposits made to the treasury.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Reports module
* Data availability within the selected date range

**Steps:**
1. Navigate to the Reports menu in the left sidebar.
2. Select 'Treasury Deposit Report' from the MIS Report list.
3. Enter the 'From Date'.
4. Enter the 'To Date'.
5. Click the 'View' button.

**Fields and controls:**
* **From Date:** The start date for the treasury deposit record search.
* **To Date:** The end date for the treasury deposit record search.

**Expected result:** The system displays the list of treasury deposits for the selected date range, or a 'Data Not Found' message if no records are available.

**Warnings:**
* A 'Data Not Found' message indicates no treasury records exist for the specified date range.

**Search keywords:** deposit, treasury, bank deposit

## 5. Tax Accounting Module

### Page: Adjustment Journal

![Adjustment Journal: Screen](screenshots/tax_accounting/adjustment_journal.png)

**Page purpose:** This page is intended to display the Adjustment Journal records for tax accounting.

**Route:** `/tax-accounting/financials/adjustmentjournal`

<!-- manual-meta: {"module": "Tax Accounting", "page": "Adjustment Journal", "task": "Access Adjustment Journal", "action": "view", "roles": [], "route": "/tax-accounting/financials/adjustmentjournal", "screenshots": ["screenshots/tax_accounting/adjustment_journal.png"], "keywords": ["journal", "adjustment", "accounting"], "task_order": 1} -->
#### Task: Access Adjustment Journal

**Purpose:** To view adjustment journal records.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has a valid account
* User is logged in

**Steps:**
1. Navigate to the Tax Accounting module
2. Click on Financials
3. Select Adjustment Journal

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** The system displays the adjustment journal page.

**Warnings:**
* The page currently returns a 404 error.

**Search keywords:** journal, adjustment, accounting

### Page: Bank Journal

![Bank Journal: Screen](screenshots/tax_accounting/bank_journal.png)

**Page purpose:** This page is intended to display the Bank Journal records for tax accounting.

**Route:** `/tax-accounting/financials/bankjournal`

<!-- manual-meta: {"module": "Tax Accounting", "page": "Bank Journal", "task": "Access Bank Journal", "action": "view", "roles": [], "route": "/tax-accounting/financials/bankjournal", "screenshots": ["screenshots/tax_accounting/bank_journal.png"], "keywords": ["journal", "bank", "accounting"], "task_order": 1} -->
#### Task: Access Bank Journal

**Purpose:** To view bank journal records.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has a valid account
* User is logged in

**Steps:**
1. Navigate to the Tax Accounting module
2. Click on Financials
3. Select Bank Journal

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** The system displays the bank journal page.

**Warnings:**
* The page currently returns a 404 error.

**Search keywords:** journal, bank, accounting

### Page: Cash Journal

![Cash Journal: Screen](screenshots/tax_accounting/cash_journal.png)

**Page purpose:** This page is intended to display the Cash Journal records for tax accounting.

**Route:** `/tax-accounting/financials/cashjournal`

<!-- manual-meta: {"module": "Tax Accounting", "page": "Cash Journal", "task": "Access Cash Journal", "action": "view", "roles": [], "route": "/tax-accounting/financials/cashjournal", "screenshots": ["screenshots/tax_accounting/cash_journal.png"], "keywords": ["journal", "cash", "accounting"], "task_order": 1} -->
#### Task: Access Cash Journal

**Purpose:** To view cash journal records.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User has a valid account
* User is logged in

**Steps:**
1. Navigate to the Tax Accounting module
2. Click on Financials
3. Select Cash Journal

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** The system displays the cash journal page.

**Warnings:**
* The page currently returns a 404 error.

**Search keywords:** journal, cash, accounting

### Page: Financials

![Financials: Screen](screenshots/tax_accounting/financials.png)

![Financials: Show](screenshots/tax_accounting/financials_show.png)

**Page purpose:** Provides access to financial report generation, specifically the Treasury Deposit Report.

**Route:** `/tax-accounting/financials`

<!-- manual-meta: {"module": "Tax Accounting", "page": "Financials", "task": "View Treasury Deposit Report", "action": "view", "roles": [], "route": "/tax-accounting/financials", "screenshots": ["screenshots/tax_accounting/financials.png", "screenshots/tax_accounting/financials_show.png"], "keywords": ["treasury", "deposit", "financial report"], "task_order": 1} -->
#### Task: View Treasury Deposit Report

**Purpose:** To retrieve and view deposit transactions within a specific date range.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User is authorized to access Tax Accounting reports

**Steps:**
1. Navigate to Tax Accounting in the side menu
2. Select Financials
3. Enter From Date
4. Enter To Date
5. Click the View button

**Fields and controls:**
* **From Date:** Start date for the report search.
* **To Date:** End date for the report search.

**Expected result:** The system displays the requested report data or indicates that no data was found.

**Warnings:**
* No specific warning was identified

**Search keywords:** treasury, deposit, financial report

### Page: Tax Accounting

![Tax Accounting: Screen](screenshots/tax_accounting/tax_accounting.png)

![Tax Accounting: Show](screenshots/tax_accounting/tax_accounting_show.png)

**Page purpose:** Landing page for the Tax Accounting module features.

**Route:** `/tax-accounting`

<!-- manual-meta: {"module": "Tax Accounting", "page": "Tax Accounting", "task": "View Tax Accounting Dashboard", "action": "view", "roles": [], "route": "/tax-accounting", "screenshots": ["screenshots/tax_accounting/tax_accounting.png", "screenshots/tax_accounting/tax_accounting_show.png"], "keywords": ["tax", "accounting", "module"], "task_order": 1} -->
#### Task: View Tax Accounting Dashboard

**Purpose:** To access various tax accounting tools and sub-modules.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User is logged into the platform

**Steps:**
1. Click on Tax Accounting in the main menu

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** The system expands or opens the Tax Accounting module options including Financials.

**Warnings:**
* No specific warning was identified

**Search keywords:** tax, accounting, module

## 6. Transaction Module

### Page: Adjustment

![Adjustment: Screen](screenshots/transaction/adjustment.png)

**Page purpose:** This page provides navigation for various adjustment types within the Transaction module.

**Route:** `/transaction/adjustment`

<!-- manual-meta: {"module": "Transaction", "page": "Adjustment", "task": "Navigate to adjustment sub-menus", "action": "view", "roles": [], "route": "/transaction/adjustment", "screenshots": ["screenshots/transaction/adjustment.png"], "keywords": ["adjustment", "debit note", "credit note", "VDS adjustment", "other adjustment"], "task_order": 1} -->
#### Task: Navigate to adjustment sub-menus

**Purpose:** Access specific adjustment modules like Debit Note, Credit Note, VDS, or Other Adjustment.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* User must be logged in

**Steps:**
1. Click on TRANSACTION in the side menu
2. Click on Adjustment to expand the list
3. Select the desired adjustment sub-menu

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** The application redirects to the selected adjustment page.

**Warnings:**
* No specific warning was identified

**Search keywords:** adjustment, debit note, credit note, VDS adjustment, other adjustment

### Page: Credit Note Adjustment

![Credit Note Adjustment: Screen](screenshots/transaction/credit_note_adjustment.png)

![Credit Note Adjustment: Show](screenshots/transaction/credit_note_adjustment_show.png)

**Page purpose:** Allows users to search and view credit note adjustments.

**Route:** `/transaction/adjustment/creditNoteAdjustment`

<!-- manual-meta: {"module": "Transaction", "page": "Credit Note Adjustment", "task": "Filter and view credit note adjustments", "action": "view", "roles": [], "route": "/transaction/adjustment/creditNoteAdjustment", "screenshots": ["screenshots/transaction/credit_note_adjustment.png", "screenshots/transaction/credit_note_adjustment_show.png"], "keywords": ["credit note", "search", "filter", "view"], "task_order": 1} -->
#### Task: Filter and view credit note adjustments

**Purpose:** To locate and review specific credit note adjustments by date range and branch.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to Transaction/Adjustment

**Steps:**
1. Navigate to Credit Note Adjustment
2. Select a branch from the dropdown
3. Enter the 'From Date' and 'To Date'
4. Click 'View'

**Fields and controls:**
* **Branch:** The business unit for the adjustment.
* **Enter From Date:** Start date for the search range.
* **Enter To Date:** End date for the search range.
* **Code Invoice Search:** Search for a specific invoice code.

**Expected result:** A table of credit note adjustments matching the search criteria appears.

**Warnings:**
* No specific warning was identified

**Search keywords:** credit note, search, filter, view

### Page: Debit Note Adjustment

![Debit Note Adjustment: Screen](screenshots/transaction/debit_note_adjustment.png)

![Debit Note Adjustment: Show](screenshots/transaction/debit_note_adjustment_show.png)

**Page purpose:** Management page for viewing and creating debit note adjustments.

**Route:** `/transaction/adjustment/debitNoteAdjustment`

<!-- manual-meta: {"module": "Transaction", "page": "Debit Note Adjustment", "task": "Search debit note adjustments", "action": "search", "roles": [], "route": "/transaction/adjustment/debitNoteAdjustment", "screenshots": ["screenshots/transaction/debit_note_adjustment.png", "screenshots/transaction/debit_note_adjustment_show.png"], "keywords": ["debit note", "search", "list"], "task_order": 1} -->
#### Task: Search debit note adjustments

**Purpose:** To find existing debit note records.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to Transaction/Adjustment

**Steps:**
1. Select the branch from the dropdown
2. Set the date range
3. Optionally enter a Debit Note Code in the search field
4. Click 'View'

**Fields and controls:**
* **Select Branch:** Select the relevant branch.
* **Debit Note Code Search:** Search by specific debit note code.

**Expected result:** Matching records populate the result table.

**Warnings:**
* No specific warning was identified

**Search keywords:** debit note, search, list

### Page: Other Adjustment

![Other Adjustment: Screen](screenshots/transaction/other_adjustment.png)

**Page purpose:** Displays miscellaneous VAT/Tax adjustments.

**Route:** `/transaction/adjustment/otherAdjustment`

<!-- manual-meta: {"module": "Transaction", "page": "Other Adjustment", "task": "View other adjustments", "action": "view", "roles": [], "route": "/transaction/adjustment/otherAdjustment", "screenshots": ["screenshots/transaction/other_adjustment.png"], "keywords": ["other adjustment", "miscellaneous", "tax records"], "task_order": 1} -->
#### Task: View other adjustments

**Purpose:** Monitor and review various tax adjustment records.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to Transaction/Adjustment

**Steps:**
1. Navigate to Other Adjustment
2. Review the generated list
3. Use pagination controls to browse records

**Fields and controls:**
* **Adjustment Code Search:** Field to filter by adjustment code.
* **rows per page:** Set the number of records displayed.

**Expected result:** A comprehensive list of adjustments is displayed with details like purpose, type, and amount.

**Warnings:**
* No specific warning was identified

**Search keywords:** other adjustment, miscellaneous, tax records

### Page: User Profile

![Transaction: Screen](screenshots/transaction/transaction.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/transaction`

<!-- manual-meta: {"module": "Transaction", "page": "User Profile", "task": "Use User Profile", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/transaction", "screenshots": ["screenshots/transaction/transaction.png"], "keywords": ["User Profile", "transaction"], "task_order": 1} -->
#### Task: Use User Profile

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the User Profile page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* No specific fields were identified from the available evidence.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** User Profile, transaction

### Page: VDS Adjustment

![Treasury And Others: Screen](screenshots/transaction/treasury_and_others.png)

![Treasury And Others: Show](screenshots/transaction/treasury_and_others_show.png)

**Page purpose:** This page contains the controls and information shown in the captured interface.

**Route:** `https://devprimevat.ibos.io/transaction/treasuryAndOthers`

<!-- manual-meta: {"module": "Transaction", "page": "VDS Adjustment", "task": "Use VDS Adjustment", "action": "view", "roles": [], "route": "https://devprimevat.ibos.io/transaction/treasuryAndOthers", "screenshots": ["screenshots/transaction/treasury_and_others.png", "screenshots/transaction/treasury_and_others_show.png"], "keywords": ["VDS Adjustment", "treasury and others"], "task_order": 1} -->
#### Task: Use VDS Adjustment

**Purpose:** Review and use the visible page functions.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* None identified from the interface

**Steps:**
1. Open the VDS Adjustment page.
2. Review the visible controls, fields, and table columns.
3. Choose the required available action for your work.

**Fields and controls:**
* **From Date:** Visible date control.
* **To Date:** Visible date control.
* **Pending:** Visible radio control.
* **Complete:** Visible radio control.

**Expected result:** The requested page information or form is displayed.

**Warnings:**
* Only actions visible in the captured interface are documented.

**Search keywords:** VDS Adjustment, treasury and others

### Page: Treasury Deposit

![Treasury Deposit: Screen](screenshots/transaction/treasury_deposit.png)

**Page purpose:** Manages records of treasury deposits and challan details.

**Route:** `/transaction/treasuryAndOthers/treasuryDeposit`

<!-- manual-meta: {"module": "Transaction", "page": "Treasury Deposit", "task": "Search treasury deposits", "action": "search", "roles": [], "route": "/transaction/treasuryAndOthers/treasuryDeposit", "screenshots": ["screenshots/transaction/treasury_deposit.png"], "keywords": ["treasury deposit", "challan", "search"], "task_order": 1} -->
#### Task: Search treasury deposits

**Purpose:** Locate specific treasury deposit records.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to Treasury and Others

**Steps:**
1. Enter the Treasury Code or Challan No in the search field
2. Review the table results

**Fields and controls:**
* **Tresuary Code and Challan No Search:** Input for searching specific deposit codes or challans.

**Expected result:** Filtered table results displayed based on the search query.

**Warnings:**
* No specific warning was identified

**Search keywords:** treasury deposit, challan, search

### Page: Turnover Tax

![Turnover Tax: Screen](screenshots/transaction/turnover_tax.png)

![Turnover Tax: Show](screenshots/transaction/turnover_tax_show.png)

**Page purpose:** Tool for viewing turnover tax-related transactions.

**Route:** `/transaction/treasuryAndOthers/turnoverTax`

<!-- manual-meta: {"module": "Transaction", "page": "Turnover Tax", "task": "Filter turnover tax transactions", "action": "filter", "roles": [], "route": "/transaction/treasuryAndOthers/turnoverTax", "screenshots": ["screenshots/transaction/turnover_tax.png", "screenshots/transaction/turnover_tax_show.png"], "keywords": ["turnover tax", "filter"], "task_order": 1} -->
#### Task: Filter turnover tax transactions

**Purpose:** Review turnover tax entries for a specific branch and time period.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to Treasury and Others

**Steps:**
1. Select the branch
2. Set the date range
3. Click 'View'

**Fields and controls:**
* **Select Branch:** Filter by business branch.
* **Enter From Date:** Start of search period.
* **Enter To Date:** End of search period.

**Expected result:** Table displays relevant turnover tax data.

**Warnings:**
* No specific warning was identified

**Search keywords:** turnover tax, filter

### Page: VDS Adjustment

![Vds Adjustment: Screen](screenshots/transaction/vds_adjustment.png)

![Vds Adjustment: Show](screenshots/transaction/vds_adjustment_show.png)

**Page purpose:** This page allows users to view and manage adjustments related to VAT Deducted at Source (VDS).

**Route:** `/transaction/adjustment/vdsAdjustment`

<!-- manual-meta: {"module": "Transaction", "page": "VDS Adjustment", "task": "Filter VDS adjustments", "action": "filter", "roles": [], "route": "/transaction/adjustment/vdsAdjustment", "screenshots": ["screenshots/transaction/vds_adjustment.png", "screenshots/transaction/vds_adjustment_show.png"], "keywords": ["VDS", "Adjustment", "Filter", "Search", "VAT"], "task_order": 1} -->
#### Task: Filter VDS adjustments

**Purpose:** To find specific VDS adjustment records based on branch, date range, and status.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Transaction module.

**Steps:**
1. Navigate to Transaction > Adjustment > VDS Adjustment.
2. Select the 'Select Branch' from the dropdown menu.
3. Enter the date range using 'Enter From Date' and 'Enter To Date'.
4. Select a status: 'Pending' or 'Complete'.
5. Click the 'View' button to display the filtered records.

**Fields and controls:**
* **Select Branch:** Dropdown to select the company branch.
* **Enter From Date:** Start date for the filter.
* **Enter To Date:** End date for the filter.
* **Pending:** Radio button to filter records with pending status.
* **Complete:** Radio button to filter records with completed status.

**Expected result:** A list of VDS adjustment records matching the specified criteria will appear in the table.

**Warnings:**
* No specific warning was identified

**Search keywords:** VDS, Adjustment, Filter, Search, VAT

### Page: VDS Certificate (Issue)

![Vds Certificate Issue: Screen](screenshots/transaction/vds_certificate_issue.png)

![Vds Certificate Issue: Show](screenshots/transaction/vds_certificate_issue_show.png)

**Page purpose:** This page is used to view issued VAT Deduct at Source (VDS) certificates.

**Route:** `/transaction/treasuryAndOthers/varDeductatSource`

<!-- manual-meta: {"module": "Transaction", "page": "VDS Certificate (Issue)", "task": "View VDS certificates", "action": "view", "roles": [], "route": "/transaction/treasuryAndOthers/varDeductatSource", "screenshots": ["screenshots/transaction/vds_certificate_issue.png", "screenshots/transaction/vds_certificate_issue_show.png"], "keywords": ["VDS", "Certificate", "Issue", "Deduct", "VAT"], "task_order": 1} -->
#### Task: View VDS certificates

**Purpose:** To view and track issued VDS certificates for a specific period.

**Required roles:**
* No role restriction was identified

**Prerequisites:**
* Access to the Transaction module.

**Steps:**
1. Navigate to Transaction > Treasury And Others > VDS Certificate (Issue).
2. Select the branch from 'Select Branch'.
3. Specify the date range using 'Enter From Date' and 'Enter To Date'.
4. Choose a status: 'All', 'Pending', or 'Complete'.
5. Click the 'View' button.

**Fields and controls:**
* **Select Branch:** Dropdown for branch selection.
* **Enter From Date:** Start date for the period.
* **Enter To Date:** End date for the period.
* **All:** Filter by all certificate statuses.
* **Pending:** Filter by pending certificate status.
* **Complete:** Filter by completed certificate status.

**Expected result:** A table showing details like Purchase Date, Supplier Name, Certificate No, Chalan No, and Deducted Amount will be generated.

**Warnings:**
* No specific warning was identified

**Search keywords:** VDS, Certificate, Issue, Deduct, VAT
