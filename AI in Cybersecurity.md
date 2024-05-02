# AI in Cybersecurity



## Introduction

Artificial Intelligence (AI) is the ability of computer systems to perform tasks that would typically require human intelligence, such as learning, reasoning, and problem-solving. This is achieved using sophisticated AI algorithm models to process and analyze large amounts of data. The trained AI model uses patterns and insights discovered from the data to perform tasks like making predictions and generating output.

AI algorithm: An AI algorithm is a set of instructions that define *how* an AI system processes data. For example, the CNN (convolutional neural network) algorithm defines how an AI system analyzes visual imagery.

AI model: An AI model is a trained instance of an algorithm that captures the learned knowledge and is used to perform tasks. For example, a trained CNN model is used to recognize and classify new and unseen images.

As technology progresses, so do the threats posed by hackers and cyber attackers. According to the FBI Internet Crime Report, 847,376 complaints of internet-related crimes and financial losses exceeding 6.9 billion dollars, a substantial increase from the previous year.

With connected devices projected to generate a staggering 79 zettabytes of data by 2025, manual analysis by humans becomes impractical, making AI an indispensable tool in the fight against cybercrime.

AI in cybersecurity establishes secure applications by default, eliminating vulnerabilities for users. By eradicating negative defaults, AI guarantees precision in detecting issues, expediting investigations, and automating response mechanisms. AI-driven solutions, such as user verification through behavioral biometrics, foster secure app development and promote a safe data ecosystem, contributing to a robust infrastructure.

### application scenarios



#### Threat Detection and Prevention

One area where AI excels is threat detection. It can analyze large amounts of data from different sources and identify unusual patterns in users' behavior, which could indicate a cyber attack. For example, if an employee unknowingly clicks on a phishing email, AI can quickly notice the change in their behavior and alert us to a potential security breach. By automating incident response actions, such as isolating affected systems or blocking malicious activities, AI minimizes opportunities for attackers and limits the potential impact of a security breach.

#### User Behavior Analytics

AI models utilize deep and machine learning techniques to analyze network behavior and detect deviations from the norm continuously. Over time, these models self-correct and adapt, improving their accuracy in identifying anomalies and potential threats. The self-correcting nature of AI models empowers organizations with robust and reliable cybersecurity defense mechanisms capable of quickly responding to emerging cyber threats.

AI-driven behavioral analytics enhances threat-hunting processes by creating deployed application profiles and analyzing vast user and device data. This proactive approach enables organizations to identify evolving threats and vulnerabilities effectively.

#### Vulnerability Assessment and Management

As cybercriminals continuously deploy sophisticated methods, organizations struggle to manage the influx of new vulnerabilities. AI-driven solutions, such as User and Entity Behavior Analytics (UEBA), analyze device, server, and user activities to detect anomalies and zero-day attacks. By preemptively protecting against undisclosed vulnerabilities, AI enables real-time defense against high-risk threats.



### challenges of Implementing AI in cybersecurity



#### Bias in AI security systems

Just like humans, AI systems can be influenced by bias in the data they are trained on. If the training data is biased, the AI system may produce discriminatory outcomes, impacting cybersecurity decision-making. Leading AI platforms invest in ongoing and thoughtful ML training to minimize bias in their systems and ensure fairer results.

#### Privacy and legal сomplications

AI applications in cybersecurity may involve the processing and analysis of vast amounts of personally identifiable data, raising critical privacy concerns. Before deploying AI systems, a legal examination is essential to ensure compliance with privacy regulations. In some regions, AI solutions, such as ChatGPT, may face restrictions, which can complicate deploying other AI-based cybersecurity solutions in those locations.

#### Privacy and legal сomplications

AI applications in cybersecurity may involve the processing and analysis of vast amounts of personally identifiable data, raising critical privacy concerns. Before deploying AI systems, a legal examination is essential to ensure compliance with privacy regulations. In some regions, AI solutions, such as ChatGPT, may face restrictions, which can complicate deploying other AI-based cybersecurity solutions in those locations.





## Method Introduction

The most common AI algorithms used in cybersecurity include machine learning (ML) models such as MLP, LSTM, GRU, Decision Tree, SGD, KNN, and CNN . These algorithms are utilized in various aspects of cybersecurity, including access control, user authentication, behavior analysis, spam, malware, and botnet identification . Additionally, regression, clustering, and classification algorithms are also commonly used for network protection in cybersecurity . Deep learning algorithms, such as Convolutional Neural Network (CNN), Auto Encoder (AE), Deep Belief Network (DBN), Recurrent Neural Network (RNN), Generative Adversal Network (GAN), and Deep Reinforcement Learning (DIL), have also been employed in cybersecurity applications . These algorithms have shown improvements in accuracy, scalability, reliability, and performance of cybersecurity systems . Furthermore, radial basis function networks (RBFNs) and multi-layer perceptron (MLP) neural networks have been used for data analytics in network intrusion detection .



### AI techniques

#### Natural Language Processing (NLP)

Natural language processing (NLP) is a branch of AI that enables computers to understand, interpret, and generate human language. It makes use of a variety of AI and machine learning algorithms to process and analyze textual data. Trained NLP models are used for tasks like translation, text classification, named entity recognition (NER), sentiment analysis, and question-answering.

NLP plays a crucial role in detecting threats that involve language-related elements. One example is the detection of malicious domains, which attackers use to distribute malware, steal credentials, exfiltrate data, and more. A popular way attackers use to trick us into trusting malicious domains is typosquatting, more commonly known as URL hijacking. This technique involves creating domain names that are similar to legitimate ones but contain slight typographical variations, such as replacing the letter "o" with the number 0. To counteract this, we apply NLP on a large body of known domain names to learn elements like keywords, patterns, and character combinations to differentiate between benign and malicious domains. This enables security tools to identify and block malicious domains like "g00gle.com" and "paypall.com." Apart from this, NLP is an important component in defense strategies against other text-based threats, such as phishing emails, webshells, and website defacements.



#### Random Forests

A decision tree is a model used for making a prediction about a particular problem. Say you were asked to predict whether a random car will break down within the next year. You have a decision tree to help you make the prediction. The decision tree was created based on data of 1,000 "instances" of whether a car broke down or not within a year and its associated "features," such as car age, mileage, brand, service history, and driving conditions. The decision tree is modeled in a way that best represents the dataset, with the most predictive feature at the top of the tree and the least predictive feature at the bottom. To make a prediction about a new car, you simply take the features of this instance and work your way through the decision tree.

In the above example, a random forest will take many random samples of the dataset, say, 100 samples with 10 cars per sample. A decision tree is then created for each sample, with each decision tree using only a random subset of features (e.g., car age and brand for Tree 1, mileage and service history for Tree 2, and so on). The relevant features of a new car are passed through each decision tree to produce 100 predictions. In the end, the prediction with the most votes is taken as the final prediction.

Random forests can be used in various cyber security scenarios to detect whether new instances of an event are malicious. One such scenario is the detection of brute force attacks, where attackers attempt to gain unauthorized access to an account or system by trying different combinations of login credentials. A popular target of brute force attacks is the remote desktop service. To detect such attacks, a random forest algorithm is applied to learn the patterns of RDP (remote desktop protocol) logs, which record information about remote desktop connections. The random forest model can then predict whether a new remote desktop connection is malicious based on features like the number of failed login attempts, login success ratio, the time interval between login attempts, and login location. Other applications of random forests include the detection of command-and-control communication and DNS tunneling.



#### Anomaly Detection

Anomaly detection is a technique used to identify unusual or abnormal instances and patterns in a dataset. The process starts by training a machine learning model to learn the normal patterns and characteristics of a dataset. The trained model is then used to detect anomalies in new, unseen data.

Anomaly detection is a crucial technique in the detection of sophisticated threats that manage to breach the network. The idea is that, despite the stealthiness of advanced techniques, there must be ways in which they differ from normal behavior and, therefore, can be picked up by powerful anomaly detection models.

Anomaly detection systems collect traffic from across the network. They use AI and ML algorithms to analyze traffic metadata over a period of time to build baselines of normal network traffic and behavior. This can include baselines of normal behavior for users, devices, and applications using what is known as User and Entity Behavior Analytics (UEBA). The system then compares real-time traffic with the learned baselines to detect and flag anomalous traffic or behavior.

Anomaly detection is enhanced by correlation analysis. In cyber security, correlation analysis is the analysis and identification of relationships between different security events, logs, and indicators of compromise (IOCs). By learning the relationships between different data, correlation analysis enables anomaly detection to establish baselines based on the normal behavior of one indicator with respect to other indicators. This enables highly accurate detection of abnormal and suspicious network activities, resulting in low false positives.

Detecting data exfiltration is challenging because attackers employ sophisticated techniques to blend exfiltrated data within normal network traffic. These techniques include fragmenting data into smaller chunks, scheduling exfiltration during normal business hours, using different protocols, and sending data to trusted cloud storage services. Nevertheless, a powerful anomaly detection model that simultaneously analyzes multiple dimensions of network data is well-equipped to detect concealed data exfiltration. This could include traffic metadata, file and data access logs, user behavior, communication patterns, and so on. This enhanced approach improves the detection of data exfiltration, especially covert espionage operations carried out by APT  groups.



#### Graph Analysis

Graph analysis uses ML algorithms to analyze a graphical representation of relationships between a group of objects called "entities." In such a graph, each entity is depicted as a node, while the relationships between them are represented as lines or "edges." Graph analysis enables us to gain valuable insights by discovering patterns within complex networks.

Suppose you want to gain a deeper understanding of the friendships among students in a specific year group. In that case, you can plot a graph that represents the friendships, with the students as nodes and friendships as edges. You can then apply ML algorithms to analyze the graph and extract insights about the friendships. For instance, you can identify the individual with the most friends (the node with the highest number of connections) and friendship groups (multiple connections within a group of nodes).

Graph analysis can be used to address cyber security events that involve a complex web of connections. A perfect application scenario is the detection of botnets, which are intricate networks of malware-infected computers or devices controlled by a central attacker. Botnets are often used for malicious purposes like distributed denial-of-service (DDoS) attacks, malware distribution, and cryptomining. They are difficult to detect due to their ability to distribute control among numerous compromised devices, making it a challenge to identify the central source of malicious activity. Nonetheless, we can apply graph analysis on network connections to reveal insights about the relationships and patterns between devices, such as devices with a high degree of centrality or abnormal connections. Security teams can use this intelligence to identify the controlling device and mitigate the botnet.



## Benefits and drawbacks of AI in Cybersecurity



#### benefits

Some of the benefits of AI in Cybersecurity that are as follow:

1. Enhanced Threat Detection Accuracy and Faster Response Times:

   AI algorithms excel in identifying patterns and anomalies in vast amounts of data, leading to more accurate threat detection. Automated Incident Response (AIR) systems powered by AI enable organizations to respond to security incidents swiftly and effectively, reducing the impact of breaches.

2. Improved Ability to Identify Novel and Sophisticated Attacks:

   AI’s advanced analytics and machine learning capabilities empower cybersecurity systems to detect and respond to novel and sophisticated cyber threats that traditional methods may overlook. By continuously learning from past incidents, AI systems adapt to evolving attack techniques, enhancing overall security posture.

3. Reduced Workload for Security Analysts:

   AI automates routine security tasks, such as monitoring network traffic and analyzing security alerts, reducing the workload for human security analysts. This allows analysts to focus their expertise on investigating and mitigating complex security issues, improving overall efficiency and effectiveness.

4. Continuous Monitoring and Automated Responses for 24/7 Protection:

   AI-powered cybersecurity systems provide continuous monitoring and automated responses, ensuring round-the-clock protection against cyber threats. By leveraging AI’s capabilities, organizations can proactively identify and respond to security incidents in real-time, minimizing the risk of breaches and data loss.

   

#### drawbacks

While AI holds tremendous promise for revolutionizing cybersecurity, its widespread adoption also presents challenges and considerations. These include:

1. Data Privacy and Ethics

    Modern cybersecurity which is AI-based is mostly based on the history of the data which is difficult to be obtained via the training process and analysis, thus people with the data privacy, confidentiality, and ethics are the same.

2. Adversarial AI

   Some cybercriminals see AI systems as an opportunity to attack through the software vulnerabilities they may cause, for instance, the adversarial attacks that confuse machine learning and fool the detection.

3. Algorithmic Bias:

   There is the chance AI algorithms to be biased towards the data it is taught on which may lead to discriminatory actions against threats assessment or to inaccurate outcomes.

4. Human Expertise

    At the same time, AI as a cybersecurity tool brings about a high efficiency but, the human expert knowledge is more demanded in the complicated situation to assess the results, to validate the alerts, and to make right decisions.













## Conclusion and Outlook



### Future 

#### Autonomous Security Systems

AI have the potential to develop autonomous security systems that can function independently and make decisions without human intervention. This would empower organizations to promptly address threats, even in the absence of human operators.

#### Predictive Threat Intelligence

 AI can be utilized to analyze data from diverse sources and offer predictive threat intelligence. This would empower organizations to anticipate and prepare for emerging threats before they materialize.

#### Advanced Threat Hunting

AI can be employed to create advanced threat-hunting systems capable of detecting and responding to unknown threats. This would enable organizations to stay one step ahead of attackers who continuously evolve their tactics.

#### AI-Driven Incident Response And Forensics: 

AI  can automatically analyze data from various sources, such as network traffic, endpoint data, and logs, to swiftly identify and respond to threats in real time. This would enable organizations to promptly contain and investigate incidents.

#### Automated Compliance And Governance

 AI can automate the compliance and governance process by continuously monitoring and reporting on security controls, as well as identifying potential violations.





### Conclusion

AI is rapidly becoming an essential technology for boosting the effectiveness of IT security teams. The limitations of human scalability in adequately securing an enterprise-level attack surface are evident, and AI provides the crucial analysis and threat detection necessary for security professionals to mitigate breach risks and strengthen security measures. Furthermore, AI aids in the identification and prioritization of risks, guides incident response efforts, and detects malware attacks proactively.

Despite the potential drawbacks, AI will undoubtedly propel the field of cybersecurity forward and enable organizations to establish a stronger security stance.