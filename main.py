from roles import cv_creator, job_describer


def make_cv(job_description_html: str, cv_template: str) -> str:
    job_description = job_describer.JobDescriber().create_job_description(
        job_description_html
    )
    cv = cv_creator.CvCreator().create_cv(job_description, cv_template)
    return cv


if __name__ == "__main__":
    job_description_html = """
        About the job
            </h2><div class="jobs-description__content jobs-description-content
            ">
          <div class="jobs-box__html-content jobs-description-content__text t-14 t-normal
              jobs-description-content__text--stretch" id="job-details" tabindex="-1">
            <h2 class="text-heading-large">
              About the job
            </h2>
About the job
Wir sind ein erfolgreiches, mittelständisches IT Beratungsunternehmen, das sich seit mehr als 22 Jahren u.a. darauf spezialisiert hat, mit anspruchsvollen Entwicklungstätigkeiten deutschlandweit Kunden zu unterstützen.


Das erwartet Dich.

Solvatis verfügt über langjährige Kundenbeziehungen zu zahlreichen großen Unternehmen in verschiedenen Branchen. Für ein Leuchtturm-Projekt bei einem international führenden Logistik-Konzern suchen wir sofort Verstärkung für die Weiterentwicklung einer mobilen Logistik-Applikation.


Darauf kannst Du Dich freuen.

direkter Einstieg in ein TOP-Projekt der Logistik-Branche
Ein motiviertes und sympathisches Team, das Dinge anpackt.
Garantiert keine Langeweile!
Ausreichenden Freiraum zur persönlichen Weiterentwicklung.
Eine angemessene Bezahlung!


Deine Aufgaben:

Unterstützung des rund 15-köpfigen Test-Teams durch Administration, Konfiguration und Wartung von Cloud-Umgebungen - insbesondere MS Azure


Das bringst Du mit:

Experten-Wissen und -Erfahrung im Devops- und Cloudumfeld. Insbesondere mit MS Azure und Azure Devops
Erfahrung in der Anwendung von Azure Devops Tools (z.B. Boards, Testplan)
Verständnis für die Prozesse und das Doing im Software-Testing


Wir verwenden folgende Technologien und Tools, und freuen uns wenn du mit möglichst vielen bereits praktische Erfahrungen sammeln konntest:


Docker, Kubernetes, HELM
Linux
Filebeat
Oracle
MQ allgemein
Apache (Active MQ, Webserver)
Kafka
Cassandra
Rabbit MQ
Oracle Weblogic Application Server
Java
GIT/Bitbucket
Jenkins/Maven
Cucumber
SQL
Grafana
ELK (Kibana, Logstash)
Prometheus
JMeter
Shell-Programmierung
idealerweise mindestens ISTQB Foundation oder vergleichbar


Wirklich wichtig ist uns:

Lust auf Arbeit an komplexen und unternehmenskritischen Systemen
sehr gute Deutschkenntnisse
Du lachst bei der Arbeit. Täglich. Mehrmals.
           <div class="mt4">
                <span><strong><!---->We help the world run better<!----><span><br></span><span><br></span></strong></span><!---->Our company culture is focused on helping our employees enable innovation by building breakthroughs together. How? We focus every day on building the foundation for tomorrow and creating a workplace that embraces differences, values flexibility, and is aligned to our purpose-driven and future-focused work. We offer a highly collaborative, caring team environment with a strong focus on learning and development, recognition for your individual contributions, and a variety of benefit options for you to choose from. Apply now!<!----><span><br></span><span><br></span><span><strong><!---->Summary &amp; Role Information<!----><span><br></span><span><br></span></strong></span><!---->In this role you will be working in a cross-functional team who values trust, respect and diversity. Being part of a motivated team with you know the importance of communication and feedback. You are appreciated for your engagement, your constructive input and your relentless drive to improve yourself, the product and the company. We are looking for people who share our passion for creating products that people love to use. To thrive in this role, you are someone who appreciates close collaboration, open communication, and feedback<span class="white-space-pre"> </span><span><br></span><span><br></span><!---->You will be working in our empowered, agile cross-functional team, which is responsible for SAP Signavio Process Manager. As a lead engineer, you will you will play a crucial role in the solution design of our business process modeling and simulation software, with the primary objective of creating a shared understanding of application architecture and solution design, including performance at scale.<span class="white-space-pre"> </span><span><br></span><span><br></span><span><strong><!---->What you will do:<span class="white-space-pre"> </span><span><br></span><span><br></span></strong></span><span>      <ul><span><li><!---->Contribute to the technical strategy for the team to broader initiatives across all SAP Signavio teams developers<span class="white-space-pre"> </span></li></span><span><li><!---->Architect, design, and implement robust and scalable backend solutions for the SAP Signavio Process Manager.<span class="white-space-pre"> </span></li></span><span><li><!---->Lead by example through hands-on coding, code reviews, and ensuring best practices in software development.<span class="white-space-pre"> </span></li></span><span><li><!---->Collaborate with cross-functional teams to ensure seamless integration of backend services with front-end applications and other systems.<span class="white-space-pre"> </span></li></span><span><li><!---->Outline the interconnections between different business processes, fostering a holistic understanding of the system.<span class="white-space-pre"> </span></li></span><span><li><!---->Embrace agility and adaptability, ensuring the team delivers high-quality solutions within the specified timelines.<span class="white-space-pre"> </span></li></span><span><li><!---->Work in an agile development environment, contributing to sprint planning, daily stand-ups, and retrospectives.<span class="white-space-pre"> </span></li></span><span><li><!---->Invest in coaching and mentoring team members to foster their professional growth.<span class="white-space-pre"> </span></li></span><span><li><!---->Proactively identify new opportunities and advocate for and implement improvements to the current state of products and team ways of working.<span class="white-space-pre"> </span></li></span><span><li><!---->Work collaboratively with the Product Owner and Tech Lead to reach agreement on the technical commitments and actively participate in the definition functional and nonfunctional requirements (KPIs, quality &amp; understanding value chain).<span class="white-space-pre"> </span><span><br></span><span><br></span></li></span></ul>
</span><span><strong><!---->What You’ll Bring<!----><span><br></span><span><br></span></strong></span><span>      <ul><span><li><!---->A master's degree in computer science or related field, or the equivalent through a combination of education and related work experience<span class="white-space-pre"> </span></li></span><span><li><!---->6+ years of proven experience in backend development with a strong focus on scalable and distributed systems.<span class="white-space-pre"> </span></li></span><span><li><!---->Proficiency in relevant technologies such as Java, Python, or similar languages.<span class="white-space-pre"> </span></li></span><span><li><!---->Passion about crafting clean and well tested code<span class="white-space-pre"> </span></li></span><span><li><!---->Demonstrated experience with safely and efficiently refactoring larger pieces of code<span class="white-space-pre"> </span></li></span><span><li><!---->Experience with migrating monolithic solutions to microservice based architectures<span class="white-space-pre"> </span></li></span><span><li><!---->Hands-on experience with NoSQL or SQL databases. It would be even better if you have experience in DB related optimizations<span class="white-space-pre"> </span></li></span><span><li><!---->Experience working with Docker, Kubernetes, and related cloud technologies is a huge plus<span class="white-space-pre"> </span></li></span><span><li><!---->Strong communication skills and the ability to collaborate across diverse teams.<span class="white-space-pre"> </span></li></span><span><li><!---->Fluent English language skills are mandatory<span class="white-space-pre"> </span><span><br></span><span><br></span></li></span></ul>
</span><span class="white-space-pre"> </span><!----><!----><span><br></span><span><br></span><span><strong><!---->Meet your team<span class="white-space-pre"> </span><span><br></span><span><br></span></strong></span><!---->Building on the intelligent enterprise strategy, SAP Signavio set out to support and accompany SAP customers in navigating through their digital transformation by helping them understand and improve their business processes.<!----><span><br></span><span><br></span><!---->The Business Modeling and Workflow (BM&amp;W) group is one of five groups in the engineering department of the SAP Signavio unit. We value consistency, modularity &amp; re-usability, as well as simplicity. We strive for a coherent user experience across the entire product suite and an effective &amp; efficient cross-product development experience. To this effect, our teams deliver SAP Signavio core products such as the SAP Signavio Process Manager or SAP Signavio Governance components.<!----><span><br></span><span><br></span><!---->#SAPBPICareers #businessprocessintelligence #signavio #bpi #MultiSalesDE #Signavio_PE #ICC24<!----><span><br></span><span><br></span><span><strong><!---->We build breakthroughs together<!----><span><br></span><span><br></span></strong></span><!---->SAP innovations help more than 400,000 customers worldwide work together more efficiently and use business insight more effectively. Originally known for leadership in enterprise resource planning (ERP) software, SAP has evolved to become a market leader in end-to-end business application software and related services for database, analytics, intelligent technologies, and experience management. As a cloud company with 200 million users and more than 100,000 employees worldwide, we are purpose-driven and future-focused, with a highly collaborative team ethic and commitment to personal development. Whether connecting global industries, people, or platforms, we help ensure every challenge gets the solution it deserves. At SAP, we build breakthroughs, together.<!----><span><br></span><span><br></span><span><strong><!---->We win with inclusion<!----><span><br></span><span><br></span></strong></span><!---->SAP’s culture of inclusion, focus on health and well-being, and flexible working models help ensure that everyone – regardless of background – feels included and can run at their best. At SAP, we believe we are made stronger by the unique capabilities and qualities that each person brings to our company, and we invest in our employees to inspire confidence and help everyone realize their full potential. We ultimately believe in unleashing all talent and creating a better and more equitable world.<!----><span><br></span><span><br></span><!---->SAP is proud to be an equal opportunity workplace and is an affirmative action employer. We are committed to the values of Equal Employment Opportunity and provide accessibility accommodations to applicants with physical and/or mental disabilities. If you are interested in applying for employment with SAP and are in need of accommodation or special assistance to navigate our website or to complete your application, please send an e-mail with your request to Recruiting Operations Team: Careers@sap.com.<!----><span><br></span><span><br></span><!---->For SAP employees: Only permanent roles are eligible for the SAP Employee Referral Program, according to the eligibility rules set in the SAP Referral Policy. Specific conditions may apply for roles in Vocational Training.<!----><span><br></span><span><br></span><!---->Requisition ID: 387263 | Work Area: Software-Design and Development | Expected Travel: 0 - 10% | Career Status: Professional | Employment Type: Regular Full Time | Additional Locations:<!----><span><br></span><span><br></span>
           </div>
          </div>
          <div class="jobs-description__details">
         </div>
        </div> 
        """
    cv_template = """
        Skills:

Professional Experience:
⦁ Senior Back End Engineer, ArtNight (Berlin, Germany), Feb 2023 - Jan 2024
⦁ Engineer, SoundCloud (Berlin Metropolitan Area), Jan 2019 - Jan 2023
⦁ Senior Software Engineer, Truecaller (Stockholm, Sweden), Jun 2018 - Dec 2018
⦁ Senior Software Developer, AVITO.ru (Moscow, Russian Federation), Aug 2017 - Jun 2018
⦁ Software Developer, Yandex (Moscow, Russian Federation), Jul 2016 - Aug 2017
⦁ Senior Software Engineer, MERA Software Services (Nizhny Novgorod Region, Russian Federation), Jun 2011 - Jun 2016
    """
    print(make_cv(job_description_html, cv_template))
