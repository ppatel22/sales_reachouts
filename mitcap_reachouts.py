# %%
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import pandas as pd
import datetime
from env_variables import no_no_list, reached_df, sample_df

# %% Set your email server details
smtp_server = "outgoing.mit.edu"
smtp_port = 25
email_address = "***@mit.edu"  # Use your actual MIT email address

try:
    # Create an SMTP session
    smtp_session = smtplib.SMTP(smtp_server, smtp_port)

    # If the connection is successful, print a success message
    print("Connected to the email server.")

    # Close the SMTP session
    smtp_session.quit()

except smtplib.SMTPException as e:
    # If there's an error during the connection, print an error message
    print("Error: Unable to connect to the email server.", str(e))


# %% List of recipient email addresses
vc_database_path = "master_list.csv"
vcs_df = pd.read_csv(vc_database_path)

cc_emails = ["laraoz@mit.edu", "timmyd@mit.edu"]

subject = "Working with MIT’s VC club?"

pdf_file_path = "Collegiate-Prospectus.pdf"
sent_df = pd.DataFrame(
    columns=[
        "My name",
        "Reach-Out Date",
        "VC Firm",
        "VC Contact Name",
        "VC Contact Email",
    ]
)
condition1 = pd.isna(vcs_df["companies"])
condition2 = vcs_df["companies"].isin(no_no_list)
condition3 = vcs_df["companies"].isin(reached_df["Firm Name"])
condition4 = vcs_df["Fund type"].isin(["Venture Fund", "Corporate VC"])
filtered_df = vcs_df[~(condition1 | condition2 | condition3) & condition4]
# %%Create an SMTP session
smtp_session = smtplib.SMTP(smtp_server, smtp_port)

for index, entry in filtered_df.iterrows():
    msg = MIMEMultipart()
    msg["From"] = email_address
    msg["To"] = entry["emails"]
    msg["Cc"] = ", ".join(cc_emails)
    msg["Subject"] = subject
    vc_name = entry["companies"]
    firstName = entry["firstname"].split(" ")[0]
    body = f"Hi {firstName}!\n\nMy name is ***FIRSTNAME, and I'm one of the leaders of MIT's top VC/startup organizations, MIT Undergraduate Capital Partners. We’re part of Collegiate Capital Partners, a student organization dedicated to increasing student access to VC through hands-on investing experience, and I’m writing to see if we might find a fit to work with {vc_name} through one of our programs.\n\nOur two main value-adds:\n \u2022 Our diligence program pairs a team of students with a partner VC firm’s investment team, helping with deal flow and using resources exclusive to our university and student perspective.\n \u2022 Our sourcing program sources early startups from Harvard, MIT, Penn, Princeton, and Yale for our VC partners by leveraging partnerships, relationships, and domain expertise.\n\nOur group has worked with over 800 startups and 60+ VC firms, such as Sequoia, XFund, ACME, and DN Capital. Our members have proven experience at top VC firms, tech companies, PE firms, and financial institutions (General Catalyst, Bessemer Venture Partners, Facebook, Intel, Goldman/MS TMT) and are truly passionate about this kind of work.\n\n100% of your contribution goes towards initiatives to make a more open and diverse version of VC through student education, non-equity grants, and mentorship. We seek to nurture our university’s innovation ecosystem, and in addition to our diligence and sourcing programs, we offer partner firms like yours several opportunities for branding and campus recruiting.\n\nI’ve attached our information packet below for your reference—let me know if this sounds like a good fit for {vc_name}, and I’d love to chat!\n\nBest,\n***FULLNAME"
    msg.attach(MIMEText(body, "plain"))

    print("Preview of the email:")
    print(subject)
    print(msg["To"])
    print(body)
    send_email = input("Do you want to send this email? (y/n/q): ")
    if send_email.lower() == "y":
        with open(pdf_file_path, "rb") as pdf_file:
            pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
        pdf_attachment.add_header(
            "Content-Disposition", f"attachment; filename=Collegiate-Prospectus.pdf"
        )
        msg.attach(pdf_attachment)
        smtp_session.sendmail(email_address, entry["emails"], msg.as_string())
        print("Email sent.")
        sent_df.loc[len(sent_df)] = {
            "My name": "***FULLNAME",
            "Reach-Out Date": datetime.datetime.now().strftime("%m/%d/%Y"),
            "VC Firm": vc_name,
            "VC Contact Name": entry["firstname"],
            "VC Contact Email": entry["emails"],
        }
    elif send_email.lower() == "q":
        print("Quit application.")
        break
    else:
        print("Email not sent. Skipped.")

# Close the SMTP session
smtp_session.quit()

print("Emails sent successfully!")
sent_df.to_csv("personal_Reach-Outs.csv", index=False)
# %%
