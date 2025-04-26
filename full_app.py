# import streamlit as st
# import pandas as pd
# import os
# from datetime import datetime
# import glob

# # Set page config
# st.set_page_config(
#     page_title="Student Attendance Tracker",
#     layout="wide"
# )

# # App title
# st.title("Student Attendance Tracker")

# # Function to load batch data
# def load_batch_data(batch_file):
#     try:
#         # Try reading with different engines in case one fails
#         try:
#             df = pd.read_excel(batch_file)
#         except:
#             df = pd.read_excel(batch_file, engine='openpyxl')
        
#         # Ensure there's a column that contains student names
#         # Look for common column names that might contain student names
#         possible_name_columns = ['Name', 'Student Name', 'Full Name', 'Student', 'Student_Name']
        
#         for col in possible_name_columns:
#             if col in df.columns:
#                 return df[col].tolist()
        
#         # If no standard name column found, use the first column
#         return df.iloc[:, 0].tolist()
#     except Exception as e:
#         st.error(f"Error loading batch file: {str(e)}")
#         return []

# # Sidebar for batch selection
# st.sidebar.header("Select Batch")

# # Get all Excel files in the current directory
# excel_files = glob.glob("*.xlsx") + glob.glob("*.xls")

# if not excel_files:
#     st.sidebar.warning("No Excel files found in the current directory.")
#     st.stop()

# selected_batch = st.sidebar.selectbox(
#     "Choose a batch file:", 
#     excel_files
# )

# # Current date
# today = datetime.now().strftime("%Y-%m-%d")
# date_selected = st.sidebar.date_input("Select date for attendance", datetime.now())
# formatted_date = date_selected.strftime("%Y-%m-%d")

# # Load student names from the selected batch
# if selected_batch:
#     student_names = load_batch_data(selected_batch)
    
#     if not student_names:
#         st.error("No student names found in the selected file.")
#         st.stop()
    
#     # Main panel for attendance marking
#     st.header(f"Attendance for {selected_batch} - {formatted_date}")
    
#     # Create attendance form
#     with st.form("attendance_form"):
#         # Dictionary to store attendance status for each student
#         attendance = {}
        
#         # Create columns for better layout
#         col1, col2 = st.columns([3, 1])
        
#         with col1:
#             st.subheader("Student Name")
#         with col2:
#             st.subheader("Attendance")
        
#         # Create attendance checkboxes for each student
#         for student in student_names:
#             col1, col2 = st.columns([3, 1])
            
#             with col1:
#                 st.write(student)
#             with col2:
#                 attendance[student] = st.checkbox("Present", key=f"att_{student}", value=True)
        
#         # Submit button
#         submit_button = st.form_submit_button("Submit Attendance")
        
#         if submit_button:
#             # Create attendance DataFrame
#             attendance_data = []
            
#             for student, is_present in attendance.items():
#                 attendance_data.append({
#                     "Student Name": student,
#                     "Date": formatted_date,
#                     "Status": "Present" if is_present else "Absent"
#                 })
            
#             attendance_df = pd.DataFrame(attendance_data)
            
#             # Check if attendance file already exists
#             attendance_file = f"attendance_records_{selected_batch.split('.')[0]}.xlsx"
            
#             if os.path.exists(attendance_file):
#                 # Read existing attendance
#                 try:
#                     existing_df = pd.read_excel(attendance_file)
                    
#                     # Check if we have attendance for this date already
#                     date_exists = (existing_df["Date"] == formatted_date).any()
                    
#                     if date_exists:
#                         # Update existing records for this date
#                         existing_df = existing_df[existing_df["Date"] != formatted_date]
#                         updated_df = pd.concat([existing_df, attendance_df], ignore_index=True)
#                     else:
#                         # Add new records
#                         updated_df = pd.concat([existing_df, attendance_df], ignore_index=True)
                    
#                     updated_df.to_excel(attendance_file, index=False)
#                 except Exception as e:
#                     st.error(f"Error updating attendance file: {str(e)}")
#                     attendance_df.to_excel(attendance_file, index=False)
#             else:
#                 # Create new attendance file
#                 attendance_df.to_excel(attendance_file, index=False)
            
#             st.success(f"Attendance for {formatted_date} has been recorded successfully!")
            
#             # Display the current attendance record
#             st.subheader("Attendance Record")
#             st.dataframe(attendance_df)
            
#             # Provide download link
#             st.download_button(
#                 label="Download Attendance Sheet",
#                 data=open(attendance_file, 'rb').read(),
#                 file_name=attendance_file,
#                 mime="application/vnd.ms-excel"
#             )

















# import streamlit as st
# import pandas as pd
# import os
# from datetime import datetime
# import glob

# # Set page config
# st.set_page_config(
#     page_title="Student Attendance Tracker",
#     layout="wide"
# )

# # App title
# st.title("Student Attendance Tracker")

# # Function to load batch data
# def load_batch_data(batch_file):
#     try:
#         # Try reading with different engines in case one fails
#         try:
#             df = pd.read_excel(batch_file)
#         except:
#             df = pd.read_excel(batch_file, engine='openpyxl')
        
#         # Ensure there's a column that contains student names
#         # Look for common column names that might contain student names
#         possible_name_columns = ['Name', 'Student Name', 'Full Name', 'Student', 'Student_Name']
        
#         for col in possible_name_columns:
#             if col in df.columns:
#                 return df[col].tolist()
        
#         # If no standard name column found, use the first column
#         return df.iloc[:, 0].tolist()
#     except Exception as e:
#         st.error(f"Error loading batch file: {str(e)}")
#         return []

# # Sidebar for batch selection
# st.sidebar.header("Select Batch")

# # Get all Excel files in the current directory
# excel_files = glob.glob("*.xlsx") + glob.glob("*.xls")

# if not excel_files:
#     st.sidebar.warning("No Excel files found in the current directory.")
#     st.stop()

# selected_batch = st.sidebar.selectbox(
#     "Choose a batch file:", 
#     excel_files
# )

# # Current date
# today = datetime.now().strftime("%Y-%m-%d")
# date_selected = st.sidebar.date_input("Select date for attendance", datetime.now())
# formatted_date = date_selected.strftime("%Y-%m-%d")

# # Load student names from the selected batch
# if selected_batch:
#     student_names = load_batch_data(selected_batch)
    
#     if not student_names:
#         st.error("No student names found in the selected file.")
#         st.stop()
    
#     # Main panel for attendance marking
#     st.header(f"Attendance for {selected_batch} - {formatted_date}")
    
#     # Create attendance form
#     with st.form("attendance_form"):
#         # Dictionary to store attendance status for each student
#         attendance = {}
        
#         # Create columns for better layout
#         col1, col2 = st.columns([3, 1])
        
#         with col1:
#             st.subheader("Student Name")
#         with col2:
#             st.subheader("Attendance")
        
#         # Create attendance checkboxes for each student
#         for student in student_names:
#             col1, col2 = st.columns([3, 1])
            
#             with col1:
#                 st.write(student)
#             with col2:
#                 attendance[student] = st.checkbox("Present", key=f"att_{student}", value=True)
        
#         # Submit button
#         submit_button = st.form_submit_button("Submit Attendance")
    
#     # Variable to track if attendance has been submitted
#     attendance_submitted = False
#     attendance_file = f"attendance_records_{selected_batch.split('.')[0]}.xlsx"
    
#     if submit_button:
#         # Create attendance DataFrame
#         attendance_data = []
        
#         for student, is_present in attendance.items():
#             attendance_data.append({
#                 "Student Name": student,
#                 "Date": formatted_date,
#                 "Status": "Present" if is_present else "Absent"
#             })
        
#         attendance_df = pd.DataFrame(attendance_data)
        
#         # Check if attendance file already exists
#         if os.path.exists(attendance_file):
#             # Read existing attendance
#             try:
#                 existing_df = pd.read_excel(attendance_file)
                
#                 # Check if we have attendance for this date already
#                 date_exists = (existing_df["Date"] == formatted_date).any()
                
#                 if date_exists:
#                     # Update existing records for this date
#                     existing_df = existing_df[existing_df["Date"] != formatted_date]
#                     updated_df = pd.concat([existing_df, attendance_df], ignore_index=True)
#                 else:
#                     # Add new records
#                     updated_df = pd.concat([existing_df, attendance_df], ignore_index=True)
                
#                 updated_df.to_excel(attendance_file, index=False)
#             except Exception as e:
#                 st.error(f"Error updating attendance file: {str(e)}")
#                 attendance_df.to_excel(attendance_file, index=False)
#         else:
#             # Create new attendance file
#             attendance_df.to_excel(attendance_file, index=False)
        
#         st.success(f"Attendance for {formatted_date} has been recorded successfully!")
        
#         # Display the current attendance record
#         st.subheader("Attendance Record")
#         st.dataframe(attendance_df)
        
#         # Set flag that attendance was submitted
#         attendance_submitted = True
    
#     # Download button outside the form
#     if os.path.exists(attendance_file):
#         with open(attendance_file, "rb") as file:
#             st.download_button(
#                 label="Download Attendance Sheet",
#                 data=file.read(),
#                 file_name=attendance_file,
#                 mime="application/vnd.ms-excel"
#             )











# import streamlit as st
# import pandas as pd
# import os
# from datetime import datetime
# import glob

# # Set page config
# st.set_page_config(
#     page_title="Student Attendance Tracker",
#     layout="wide"
# )

# # App title
# st.title("Student Attendance Tracker")

# # Function to load batch data
# def load_batch_data(batch_file):
#     try:
#         # Try reading with different engines in case one fails
#         try:
#             df = pd.read_excel(batch_file)
#         except:
#             df = pd.read_excel(batch_file, engine='openpyxl')
        
#         # Ensure there's a column that contains student names
#         # Look for common column names that might contain student names
#         possible_name_columns = ['Name', 'Student Name', 'Full Name', 'Student', 'Student_Name']
        
#         name_column = None
#         for col in possible_name_columns:
#             if col in df.columns:
#                 name_column = col
#                 break
        
#         # If no standard name column found, use the first column
#         if name_column is None:
#             name_column = df.columns[0]
            
#         return df, name_column
#     except Exception as e:
#         st.error(f"Error loading batch file: {str(e)}")
#         return None, None

# # Sidebar for batch selection
# st.sidebar.header("Select Batch")

# # Get all Excel files in the current directory
# excel_files = glob.glob("*.xlsx") + glob.glob("*.xls")

# if not excel_files:
#     st.sidebar.warning("No Excel files found in the current directory.")
#     st.stop()

# selected_batch = st.sidebar.selectbox(
#     "Choose a batch file:", 
#     excel_files
# )

# # Current date
# date_selected = st.sidebar.date_input("Select date for attendance", datetime.now())
# formatted_date = date_selected.strftime("%Y-%m-%d")

# # Load student data from the selected batch
# if selected_batch:
#     batch_df, name_column = load_batch_data(selected_batch)
    
#     if batch_df is None or name_column is None:
#         st.error("Error processing the selected file.")
#         st.stop()
    
#     if batch_df.empty:
#         st.error("No student data found in the selected file.")
#         st.stop()
    
#     student_names = batch_df[name_column].tolist()
    
#     # Main panel for attendance marking
#     st.header(f"Attendance for {selected_batch} - {formatted_date}")
    
#     # Check if attendance for this date already exists
#     date_column_exists = formatted_date in batch_df.columns
    
#     if date_column_exists:
#         st.warning(f"Attendance for {formatted_date} already exists. Submitting will overwrite previous records.")
    
#     # Create attendance form
#     with st.form("attendance_form"):
#         # Dictionary to store attendance status for each student
#         attendance = {}
        
#         # Create columns for better layout
#         col1, col2 = st.columns([3, 1])
        
#         with col1:
#             st.subheader("Student Name")
#         with col2:
#             st.subheader("Attendance")
        
#         # Create attendance checkboxes for each student
#         for idx, student in enumerate(student_names):
#             col1, col2 = st.columns([3, 1])
            
#             with col1:
#                 st.write(student)
#             with col2:
#                 # If attendance for this date exists, use previous value as default
#                 default_value = True
#                 if date_column_exists:
#                     try:
#                         default_value = batch_df.at[idx, formatted_date] == "Present"
#                     except:
#                         default_value = True
                
#                 attendance[student] = st.checkbox("Present", key=f"att_{student}", value=default_value)
        
#         # Submit button
#         submit_button = st.form_submit_button("Submit Attendance")
    
#     if submit_button:
#         # Update the batch dataframe with attendance data
#         batch_df[formatted_date] = "Absent"  # Default all to absent
        
#         # Update with actual attendance
#         for idx, student in enumerate(student_names):
#             batch_df.at[idx, formatted_date] = "Present" if attendance[student] else "Absent"
        
#         # Save the updated dataframe back to the Excel file
#         try:
#             # Create a backup of the original file
#             backup_file = f"backup_{selected_batch}"
#             batch_df.to_excel(backup_file, index=False)
            
#             # Save the updated file
#             batch_df.to_excel(selected_batch, index=False)
            
#             st.success(f"Attendance for {formatted_date} has been recorded successfully!")
            
#             # Display the current batch with attendance
#             st.subheader("Updated Attendance Record")
#             st.dataframe(batch_df)
#         except Exception as e:
#             st.error(f"Error saving attendance: {str(e)}")
#             st.info(f"A backup of your data was attempted at {backup_file}")
    
#     # Download button outside the form
#     if os.path.exists(selected_batch):
#         with open(selected_batch, "rb") as file:
#             st.download_button(
#                 label="Download Updated Attendance Sheet",
#                 data=file.read(),
#                 file_name=f"updated_{selected_batch}",
#                 mime="application/vnd.ms-excel"
#             )

















import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta
import glob
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import urllib.parse
import base64

# Set page config
st.set_page_config(
    page_title="Student Attendance Tracker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# App title
st.title("Student Attendance Tracker")

# Function to load batch data
def load_batch_data(batch_file):
    try:
        # Try reading with different engines in case one fails
        try:
            df = pd.read_excel(batch_file)
        except:
            df = pd.read_excel(batch_file, engine='openpyxl')
        
        # Ensure there's a column that contains student names
        # Look for common column names that might contain student names
        possible_name_columns = ['Name', 'Student Name', 'Full Name', 'Student', 'Student_Name']
        
        name_column = None
        for col in possible_name_columns:
            if col in df.columns:
                name_column = col
                break
        
        # If no standard name column found, use the first column
        if name_column is None:
            name_column = df.columns[0]
            
        return df, name_column
    except Exception as e:
        st.error(f"Error loading batch file: {str(e)}")
        return None, None

def initialize_whatsapp_driver():
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--headless')
        
        # Uncomment the line below if you want to run in headless mode (no UI)
        # chrome_options.add_argument("--headless")
        
        # Initialize the driver with webdriver-manager for automatic chromedriver download
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Open WhatsApp Web
        driver.get("https://web.whatsapp.com/")
        
        # Wait for user to scan QR code
        st.info("Please scan the QR code on the opened browser window to log in to WhatsApp Web")
        
        # Wait for the WhatsApp page to load completely
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
        )
        
        st.success("Successfully logged in to WhatsApp Web!")
        return driver
    except Exception as e:
        st.error(f"Error initializing WhatsApp Web: {str(e)}")
        return None

# Function to send WhatsApp message using Selenium
def send_whatsapp_message_selenium(driver, phone_number, message):
    """Send WhatsApp message using Selenium automation"""
    try:
        # Format the phone number (remove any non-numeric characters)
        formatted_phone = ''.join(filter(str.isdigit, phone_number))
        
        # Make sure the phone number has the country code
        if len(formatted_phone) <= 10:  # Assuming Indian numbers
            formatted_phone = "91" + formatted_phone
        
        # Encode the message for URL
        encoded_message = urllib.parse.quote(message)
        
        # Use the WhatsApp direct message link
        direct_link = f"https://web.whatsapp.com/send?phone={formatted_phone}&text={encoded_message}"
        
        # Navigate to the direct message link
        driver.get(direct_link)
        
        # Wait for the chat to load
        chat_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
        )
        
        # Click the send button
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]'))
        )
        send_button.click()
        
        # Wait for the message to be sent
        time.sleep(2)
        
        return True
    except TimeoutException:
        st.warning(f"Timeout while sending message to {phone_number}. The number might be invalid.")
        return False
    except Exception as e:
        st.error(f"Error sending WhatsApp message to {phone_number}: {str(e)}")
        return False

# Function to generate weekly attendance reports
def generate_weekly_reports(batch_df, name_column, phone_column):
    """Generate weekly attendance reports for all students"""
    # Get dates of the last week
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())  # Start of previous week (Monday)
    end_of_week = start_of_week + timedelta(days=6)  # End of previous week (Sunday)
    
    # Format date range for display
    start_date_str = start_of_week.strftime("%Y-%m-%d")
    end_date_str = end_of_week.strftime("%Y-%m-%d")
    
    # Find all date columns in the dataframe within the week range
    date_columns = []
    class_dates = []
    for col in batch_df.columns:
        try:
            col_date = datetime.strptime(col, "%Y-%m-%d")
            if start_of_week <= col_date <= end_of_week:
                date_columns.append(col)
                class_dates.append(col)
        except:
            continue
    
    if not date_columns:
        st.warning(f"No attendance records found for last week ({start_date_str} to {end_date_str})")
        return False
    
    # Format the class dates for the message
    class_dates_formatted = ", ".join(class_dates)
    
    # Initialize the WhatsApp driver
    driver = initialize_whatsapp_driver()
    if driver is None:
        st.error("Failed to initialize WhatsApp Web. Please try again.")
        return False
        
    # Create a progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        # Send reports to each student's parent
        total_students = len(batch_df)
        success_count = 0
        
        for idx, row in batch_df.iterrows():
            student_name = row[name_column]
            
            # Skip if no phone number
            if phone_column not in row or pd.isna(row[phone_column]):
                continue
                
            phone_number = str(row[phone_column])
            
            # Find dates when the student was absent
            absent_dates = []
            for date_col in date_columns:
                if row[date_col] == "Absent":
                    absent_dates.append(date_col)
            
            # Create appropriate message
            if absent_dates:
                absent_dates_formatted = ", ".join(absent_dates)
                message = f"Greetings from APA, the physics classes for this week were held on these dates: {class_dates_formatted} and your ward, {student_name} was absent on the following dates: {absent_dates_formatted}"
            else:
                message = f"Greetings from APA, the physics classes for this week were held on these dates: {class_dates_formatted} and your ward, {student_name} attended all classes. Keep up the good work!"
            
            # Send the message
            if send_whatsapp_message_selenium(driver, phone_number, message):
                success_count += 1
            
            # Update progress
            progress = (idx + 1) / total_students
            progress_bar.progress(progress)
            status_text.text(f"Processing {idx+1}/{total_students} students...")
            
            # Small delay between messages to avoid rate limiting
            time.sleep(1)
        
        status_text.text(f"Sent {success_count} out of {total_students} reports successfully!")
        return True
    
    except Exception as e:
        st.error(f"Error sending weekly reports: {str(e)}")
        return False
    finally:
        # Close the driver
        try:
            driver.quit()
        except:
            pass

# Sidebar for batch selection
st.sidebar.header("Select Batch")

# Get all Excel files in the current directory
excel_files = glob.glob("*.xlsx") + glob.glob("*.xls")

if not excel_files:
    st.sidebar.warning("No Excel files found in the current directory.")
    st.stop()

selected_batch = st.sidebar.selectbox(
    "Choose a batch file:", 
    excel_files
)

# Current date
date_selected = st.sidebar.date_input("Select date for attendance", datetime.now())
formatted_date = date_selected.strftime("%Y-%m-%d")

# Tabs for different functionalities
tab1, tab2 = st.tabs(["Take Attendance", "Send Reports"])

# Load student data from the selected batch
if selected_batch:
    batch_df, name_column = load_batch_data(selected_batch)
    
    if batch_df is None or name_column is None:
        st.error("Error processing the selected file.")
        st.stop()
    
    if batch_df.empty:
        st.error("No student data found in the selected file.")
        st.stop()
    
    student_names = batch_df[name_column].tolist()
    
    # Tab 1: Attendance Taking
    with tab1:
        # Main panel for attendance marking
        st.header(f"Attendance for {selected_batch} - {formatted_date}")
        
        # Check if attendance for this date already exists
        date_column_exists = formatted_date in batch_df.columns
        
        if date_column_exists:
            st.warning(f"Attendance for {formatted_date} already exists. Submitting will overwrite previous records.")
        
        # Create attendance form
        with st.form("attendance_form"):
            # Dictionary to store attendance status for each student
            attendance = {}
            
            # Create columns for better layout
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.subheader("Student Name")
            with col2:
                st.subheader("Attendance")
            
            # Create attendance checkboxes for each student
            for idx, student in enumerate(student_names):
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.write(student)
                with col2:
                    # If attendance for this date exists, use previous value as default
                    default_value = True
                    if date_column_exists:
                        try:
                            default_value = batch_df.at[idx, formatted_date] == "Present"
                        except:
                            default_value = True
                    
                    attendance[student] = st.checkbox("Present", key=f"att_{student}", value=default_value)
            
            # Submit button
            submit_button = st.form_submit_button("Submit Attendance")
        
        if submit_button:
            # Update the batch dataframe with attendance data
            batch_df[formatted_date] = "Absent"  # Default all to absent
            
            # Update with actual attendance
            for idx, student in enumerate(student_names):
                batch_df.at[idx, formatted_date] = "Present" if attendance[student] else "Absent"
            
            # Save the updated dataframe back to the Excel file
            try:
                # Create a backup of the original file
                backup_file = f"backup_{selected_batch}"
                batch_df.to_excel(backup_file, index=False)
                
                # Save the updated file
                batch_df.to_excel(selected_batch, index=False)
                
                st.success(f"Attendance for {formatted_date} has been recorded successfully!")
                
                # Display the current batch with attendance
                st.subheader("Updated Attendance Record")
                st.dataframe(batch_df)
            except Exception as e:
                st.error(f"Error saving attendance: {str(e)}")
                st.info(f"A backup of your data was attempted at {backup_file}")
        
        # Download button outside the form
        if os.path.exists(selected_batch):
            with open(selected_batch, "rb") as file:
                st.download_button(
                    label="Download Updated Attendance Sheet",
                    data=file.read(),
                    file_name=f"updated_{selected_batch}",
                    mime="application/vnd.ms-excel"
                )
    
    # Tab 2: Send Weekly Reports
    with tab2:
        st.header("Send Weekly Attendance Reports via WhatsApp")
        
        # Check if there's a phone number column
        phone_columns = [col for col in batch_df.columns if any(phone_term in col.lower() for phone_term in 
                        ["phone", "mobile", "contact", "whatsapp", "cell"])]
        
        if not phone_columns:
            st.error("No phone number column found in the batch file. Please ensure your file has a column with 'phone', 'mobile', 'contact', 'whatsapp', or 'cell' in its name.")
        else:
            # Let user select which column contains phone numbers
            phone_column = st.selectbox("Select the column containing parent's phone numbers:", phone_columns)
            
            # Selenium setup information
            st.subheader("WhatsApp Web Setup")
            st.info("""
            **Important Notes Before Sending Messages:**
            
            1. Make sure you have Chrome installed on your computer
            2. When you click 'Send Reports', a Chrome window will open
            3. You'll need to scan the QR code with your WhatsApp
            4. The app will automatically send messages after login
            5. Keep the browser window open during the process
            """)
            
            # Send weekly reports button
            if st.button("Send Weekly Attendance Reports"):
                with st.spinner("Setting up WhatsApp Web and sending reports..."):
                    success = generate_weekly_reports(batch_df, name_column, phone_column)
                    if success:
                        st.success("Weekly reports sent successfully!")
                    else:
                        st.error("Failed to send weekly reports. Check the error messages above.")
            
            # Warning about automation
            st.warning("""
            **WhatsApp Automation Notice:**
            
            Please be aware that automating WhatsApp messaging is against WhatsApp's Terms of Service.
            This feature is provided for educational purposes only and should be used responsibly.
            Excessive usage may result in your WhatsApp account being temporarily banned.
            """)
            
            # Preview section
            st.subheader("Message Preview")
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Sample message for a student with absences:**")
                st.code("""
Greetings from APA, the physics classes for this week were held on these dates: 2025-04-21, 2025-04-23 and your ward, John Smith was absent on the following dates: 2025-04-21
                """)
            
            with col2:
                st.markdown("**Sample message for a student with perfect attendance:**")
                st.code("""
Greetings from APA, the physics classes for this week were held on these dates: 2025-04-21, 2025-04-23 and your ward, Jane Doe attended all classes. Keep up the good work!
                """)