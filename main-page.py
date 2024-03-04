import streamlit as st

def main():
    st.title(":wave: Hi, I'm Abhiroop Sarkar")
    st.sidebar.image("cropped-profilepic.png", use_column_width=True, output_format="PNG", width=200, )

    st.sidebar.header("Navigation")
    menu_selection = st.sidebar.radio("",["Home", "Academic Details", "Research Experience", "Projects", "Skills", "Links"])

    if menu_selection == "Home":
        show_home()
    elif menu_selection == "Academic Details":
        show_academic_details()
    elif menu_selection == "Research Experience":
        show_research_experience()
    elif menu_selection == "Projects":
        show_projects()
    elif menu_selection == "Skills":
        show_skills()
    elif menu_selection == "Links":
        show_Links()

def show_home():
    st.write("### 👨‍🎓 Undergrad @ IEM, Kolkata")
    st.write("#### Research Assistant @ IEM Centre of Excellence for Cloud Computing & IoT")
    st.write("###### I'm a second-year Computer Science undergraduate deeply passionate about cryptography and computer security. With a good foundation in computer science, I'm eager to dive deeper into the field and expand my knowledge base. I thrive in team environments, where I diligently contribute and learn alongside my peers. I'm actively seeking internship opportunities in research labs to immerse myself in cryptographic research and be part of innovative projects. Looking ahead, I aspire to pursue higher studies, potentially a Ph.D., with the ultimate goal of becoming a professor in the future. 👨🏼‍🏫")
    st.write("###### Contact Info: ")
    st.write("- 📧 Mail: Abhiroop.Sarkar2022@iem.edu.in")
    st.write("- 📧 Personal mail: abhiroopsarkar2004@gmail.com")
    st.write("- 📞 Phone: (+91) 6290397585")

def show_academic_details():
    st.write("### :school: Academic Details")
    st.write("#### :mortar_board: Undergraduate")
    st.write("- ##### 👨🏻‍💻 Bachelor of Technology in Computer Science & Engineering (Artificial Intelligence & Machine Learning) ")
    st.write("- ###### Institute of Engineering & Management, Kolkata (2022-26)")
    st.write("- ###### :paperclip: GPA: 9.48 -- Sem I: 9.36, Sem II: 9.72, Sem III: 9.38")
    st.write("- ###### Departmental Rank - 6 (1st year)")
    st.write("#### :mortar_board: School")
    st.write("- ###### 12th from Hariyana Vidhya Mandir Kolkata (2022) -- 77.8%")
    st.write("- ###### 10th from St. Mary's Orphanage & Day School, Kolkata (2020) -- 92.4%")
    st.write("During the year 2021-22, I faced overwhelming anxiety and stress. It was a dark time, reflected in my lower percentage on the 12th board and also affected my performance in competitive exams. Those days were incredibly challenging, but I've come a long way since then. I'm determined to rise above my past struggles and prove myself better.")

def show_research_experience():
    st.write("### 👨🏻‍🔬Research Experience")
    st.write("#### An Overview of the Discrete Logarithm Problem in Cryptography")
    st.write("  **Under Dr. Deepsubhra Guha Roy and Dr. Piyali Datta** -- [August 2023 - December 2023]")
    st.write("- It was my first experience in research, including the conception and implementation of a review paper.")
    st.write("- I learned how to read and understand research papers") 
    st.write("- Write conclusions after understanding the papers")
    st.write("- Gained insights into the progress of research in the domain of public-key cryptography")
    st.write("- Additionally, I learned and coded the entire paper in LaTeX")
    st.write("- Presented the first draft as a [Poster](https://www.researchgate.net/publication/375287849_The_Discrete_Logarithm_Problem)")
    st.write(" **Accepted and Presented in ICACA-2024**")
    st.write("**Abstract:** The Discrete Logarithm Problem is a computationally hard problem that is widely employed in public-key cryptography, based on the assumption that there exists no general method to efficiently solve discrete logs. In this paper, we investigate the historical evolution, theoretical foundations, associated equations, implementation techniques, applications, and security aspects of the discrete logarithm problem. A timeline detailing the early development of discrete logarithms in cryptography is presented. The algorithms deployed to solve discrete logarithm problems, including Shanks’ Baby Step-Giant Step algorithm, Pohling Hellman’s algorithm, Pollard’s Rho Algorithm, Pollard’s Kangaroo Algorithm, Index Calculus, and Function Field Sieve, are discussed. Additionally, an overview of Shor\'s quantum algorithms is provided. The paper also offers concise discussions of schemes such as Diffie Hellman key exchange, ElGamal encryption, and Elliptic curve cryptography.")
    st.write("#### AgroGenie: A smart approach to agriculture using Machine Learning")
    st.write("  **Under Dr. Piyali Datta and Dr. Deepsubhra Guha Roy** -- [July 2023 - January 2024]")
    st.write("- Worked in a team of 5 members")
    st.write("- Implemented a Crop recommendation system which achieves upto 99.6% accuracy ")
    st.write("- Implemented a novel approach of recommending clusters instead of single crops to make the system more practical")
    st.write("- Plan to implement the hardware for data collection from the farmland, and integrate with the existing system ")
    st.write("- Link to [Repository](https://github.com/Abhiroop2004/AgroGenie-A-Smart-approach-to-Agriculture-using-Machine-Learning-)")
    st.write(" **Accepted in ICISA-2024**")
    st.write("  **Abstract:** Precision agriculture is an instrumental approach for a nation whose economy is greatly influenced by agricultural yield. Crop Recommendation is a very valuable tool in the field of agriculture. This research involves the utilization of a Machine-learning-based approach to analyze the values of several parameters influencing crop growth. It then accepts a novel set of input parameters and recommends the most probable crops that can be cultivated. Adequate preprocessing methods have been applied to ensure the optimum removal of partiality from data. The ML models have been compared for their performance using a well-accepted validation measure. Then crops with similar features have been clustered to provide a more flexible farming option for the farmer.")
def show_projects():
    st.write("### Projects")
    st.write("#### 1.    Password Management System with Stream Cipher, June 2023")
    st.write("- Developed a Password Management System with robust security using Stream Cipher algorithms and PBKDF2 key derivation function")
    st.write("- Ensured secure storage of encrypted passwords and sensitive data in a binary file")
    st.write("- Implemented password changing and provided a simple and user-friendly interface for secure password management")
    st.write("- Link to [Repository](https://github.com/Abhiroop2004/Password-Management-System-with-Stream-Cipher)")
    st.write("#### 2.    IoT based CO2 level monitoring system, April 2023")
    st.write("- Worked in team of 6 in designing an IoT-enabled CO2 monitoring system using components such as NodeMCU-esp8266, mq135(gas sensor), & dht-11(temperature & humidity Sensor). Used ThingSpeak to plot data from the device")
    st.write("- Worked on writing and perfecting the code and calibrating mq135")
    st.write("- Link to [ArXiv Article](https://arxiv.org/abs/2308.03780)")
    st.write("#### 3.    Data Corruption Playground, June 2023")
    st.write("- Developed a Python mini-project to simulate various data corruption techniques and demonstrate the use of hashing for integrity checks")
    st.write("- Implemented functionalities to flip random bits, modify specific bytes, introduce noise, and swap file contents, showcasing different corruption scenarios")
    st.write("- Utilized SHA-256 hash algorithm to calculate file hashes before and after corruption, enabling detection of integrity compromise")
    st.write("- Link to [Repository](https://github.com/Abhiroop2004/Data-Corruption-Playground)")
    
def show_skills():
    st.write("### Skills")
    st.write("- **Languages:** Python, C, Matlab, Latex")
    st.write("- **Subjects:** Basics of Cryptography, Discrete Mathematics, Basics of Supervised Machine Learning")
    st.write("- **Tools:** Visual Studio Code, GitHub, Canva")

def show_Links():
    st.write("### My Links")
    st.write("- ##### [LinkedIn](https://www.linkedin.com/in/abhiroop-sarkar-77b250245/)")
    st.write("- ##### [GitHub Profile](https://github.com/Abhiroop2004)")
    st.write("- ##### [Google Scholar](https://scholar.google.com/citations?user=9GIfLH8AAAAJ&hl=en)")
    st.write("- ##### [Resume](https://drive.google.com/file/d/1YAM2dHmORKycoHAKTNZM_9tHhV4g3zke/view)")

if __name__ == "__main__":
    main()
