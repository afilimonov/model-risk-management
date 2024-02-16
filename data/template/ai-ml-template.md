# Enterprise Risks with Heightened AI/ML Risks
 
## Enterprise Risk Type Definition per the Corporate Risk Taxonomy
 
### Model Risks
 
The risk associated with potential adverse consequences from decisions based on incorrect or misused
estimation outputs/methods
 
### Data Management
 
The risk associated with availability, integrity, appropriate usage and/or inadequate management of Fannie
Mae data, information, and records (including confidential, highly restricted, and personal information).
 
### Other Operational Risks
 
#### Technology Risk
 
The risk associated with failure and/or underperformance of infrastructure, technology assets or system(s)
(on/off premise).
 
### Cybersecurity (Information Security)
 
The risk associated with ineffective Information Security controls and capabilities which could result in the
Moderate, Minor, or Insignificant compromise of the confidentiality, integrity, availability of data,
technology, and business operations.
 
#### Business Resiliency
 
The risk associated with internal/external events or an individual(s) causing business and/or system
disruption and/or including damage to Fannie Mae’s physical assets causing it to be unable to continue its
business operations.
 
#### Third-Party Risk
 
The risk of failure to adequately oversee third party activities/services which could potentially expose Fannie
Mae to credit, operational, compliance, strategic and/or reputational risk.
 
#### Compliance Risks
 
The risk of legal or regulatory sanctions, damage to current or projected financial condition, damage to
business resilience, or damage to reputation resulting in nonconformance with compliance obligations.
These obligations include laws or regulations, prescribed practices, mortgage-backed security (MBS) trust
agreements, supervisory guidance, Conservator instruction, internal policies and procedures, or ethical
standards governing how the Company operates.
 
 
## Examples of How the Enterprise Risk Type is Heightened by AI/ML
 
### Model Risks
 
Black box risk, overfitting, model drift, challenges in calibration and feedback, potential biases, misuse due to
lack of understanding or misalignment, and heightened vendor model risks from increased complexity and
proprietary constraints.
 
### Data Management
 
Data accuracy, quality, use of sensitive information, appropriateness and suitability of data, data selection
and processing bias, data security, complexity and storage, adherence to data privacy regulations, and data
lineage.
 
### Other Operational Risks
 
#### Technology Risk
 
The challenges and strategies associated with integrating the proposed AI/ML use case into existing
infrastructure, technology obsolescence, scalability, and potential performance issues.
 
#### Cybersecurity (Information Security)
 
The risk of data theft, adversarial attacks, infrastructure and system security, and potential exposure to data
poisoning.
 
#### Business Resiliency
 
#### Business functions supported by AI/ML can feed into downstream business processes or other AI/ML
systems that can cause significant disruptions across the enterprise if AI/ML performance is degraded or
compromised.
 
#### Third-Party Risk
 
Third-party provided products and services—ranging from those with embedded AI/ML to cloud providers
hosting AI/ML platforms—present potential business resiliency and concentration risks if AI/ML services are
limited to a few vendors
 
#### Compliance Risks
 
The risk of legal or regulatory enforcement actions, damage to financial condition or reputation resulting from
utilizing AI/ML in a manner that does not comply with consumer protection, fair lending, privacy and
employment discrimination laws and regulations.Personal data used in AI/ML may be subject to complex
data governance and privacy laws with requirements such as anonymizing data, securing consent to use the
data, and maintaining a record of how data is used, accessed, and stored.
 
 
## Examples of Low Risk Situations for AI/ML
 
Model Risks
 
* Black Box Risk: Global Interpretability has been provided by a well-approximating surrogate model and
Local Interpretability measures have been produced for specific important examples.
 
* Overfitting:
 
   * Regularization has penalized over-parameterization
   * Hyper-parameter tuning and re-sampling techniques have prevented generalization errors from
   significantly exceeding those on training/validation datasets
 
 
* Model Drift: Model is not automatically, dynamically re-trained unless a sufficient Adjunct to the
Performance Monitoring Plan is in-place and guards against release of a model with undetected large drift
 
* Challenges in Calibration and Feedback: When additional data is accumulated for supervised learning, the
potential for the initial use of the AI/ML model to have changed the accuracy and interpretation of that
additional labelling is critically evaluated before use in re-training.
 
* Potential Biases: Data used in training has been evaluated for bias, purged of such if needed, and chosen
algorithms for training the model have not been identified as highly-prone to producing biased results.
 
* Misuse due to lack of Understanding or Misalignment: Users of the AI/ML model have been well-trained
on how to understand and appropriately use the results, and the model is not used for any purposes for which
it would be unsuitable.
 
* Heightened Vendor Model Risks: Per contractual procurement requirements, vendors have provided
sufficient information about the model and the data used in its training to ensure transparency, and those
procuring the model have taken accountability for heightened vendor model risks.
 
 
Data Management
 
* Data Accuracy:
  * There has been no manual labelling of categorical variables used in the AI/ML model
  * Data is monitored at each stage of use
  * A remediation process ensures data issues are resolved
 
 
* Quality:
  * Qualified individuals are responsible for data ownership and management
  * Clear accountability has been established within processes to address data quality
 
 
* Use of Sensitive Information: No sensitive information is used in the AI/ML model
  * Appropriateness and Suitability: Documentation of a review confirming the appropriateness and
suitability of the data used in the AI/ML model is available
  * Bias in Data Selection and Processing: Data has been screened for over-or under-representation and
proxies that could result in bias
 
* Data Security: Access to the data used to re-train or apply the AI/ML model has been secured against
internal and external threats which could compromise its integrity
 
* Complexity and Storage: The model does not require storage of large amounts of data or rapid access to
and processing of complex streams of information
 
* Adherence to Data Privacy Regulations: No information about people is used in the AI/ML model
 
* Data Lineage:
 
  * All Key Data Elements are sourced from an enterprise-sanctioned repository with contents that adhere
to strong data lineage practices for the type of data used including unstructured image or text data
types.
  * Adequate documentation of usage rights and data permissions has been compiled for each stage of data
management.
 
 
### Other Operational Risks
 
#### Technology Risk
 
* Integrating into Infrastructure: The AI/ML model only requires pre-existing elements of the Technology
Infrastructure which have well-served applications with similar needs to this AI/ML model.
 
* Technology Obsolescence: Approvals from Enterprise Architecture of the selected technology guard against
rapid obsolescence.
 
* Scalability: Infrastructure to support data storage and computing power necessary to meet operational and
business needs is available at the initial scale and is sufficiently scalable to meet likely future needs.
 
* Potential Performance Issues:
  * Testing of the in-house or third-party AI/ML tools, applications, and systems to assess integrity, security, and
business resiliency has been sufficient to identify any potential significant performance issues.
  * Technology change management practices and procedures prevent emergence of future potential
performance issues as the AI/ML technology evolves
 
#### Cybersecurity (*Information Security)
 
* Data Theft: Only publicly available data is used in the AI/ML application
  * Adversarial Attacks:
  * The AI/ML model does not ingest external data during its application
  * The AI/ML model does not require real-time, rapid availability vulnerable to denial-of-service attacks
 
* Infrastructure and System Security:
  * If the AI/ML is hosted in Cloud infrastructure, the Cloud environment meets Fannie Mae security
requirements.
  * If open-source software or models are provisioned, they adhere to open-source governance
requirements
 
* Data Poisoning: Lineage of the data used in training the model is sufficiently clear to reduce risks of data
poisoning.
 
#### Business Resiliency
 
* Downstream Business Processes:
  * No downstream business processes depend on successful operation of this AI/ML capability, or
  * Any dependent downstream business processes are protected by adequate business continuity and
in  cident response plans which have been adapted to this AI/ML context including by introducing
manual override functions if the AI/ML starts to skew results
* Downstream AI/ML systems:
  * No downstream AI/ML systems depend on successful operation of this AI/ML capability, or
  * Any dependent AI/ML systems have introduced workarounds to prevent data dependencies and other
forms of interconnectivity from severely disrupting their operability
 
#### Third-Party Risk
 
* Third-party provided products and services with embedded AI/ML:
  * This is an ancillary AI/ML usage in the sense that the AI/ML component of the third-party provided
product or service is embedded within an application with an ability to fulfill its primary purpose even if
the AI/ML component is not used
  * Contractual requirements with third-party providers of AI/ML models and data ensure transparency and
accountability with use.
* Third-party cloud providers hosting AI/ML platforms: Resiliency against outage of a single third-party
cloud provider environment is provided by hosting arrangements.
 
#### Compliance Risks
 
* Consumer Protection: The AI/ML usage does not affect consumers
* Fair Lending: The AI/ML is not used in lending activities
* Privacy: No information about people is used in the AI/ML application
* Employment Discrimination: The AI/ML usage does not affect employment outcomes
* Personal Data:
  * No personally-identifiable information is collected or used in this AI/ML application, or
  * If personally-identifiable information is collected or used in this AI/ML application, then there is sufficient
anonymization, securing consent to use, and maintaining a record of how data is used, accessed, and stored.
 
## Template for Questions to Collect Risk: Information for Proposed Production AI/ML Use
 
If active Use of AI/ML is proposed, a templated set of questions may be used to collect information needed to evaluate requests for approval. In addition to a place to answer the question, there will be a place to provide additional free-form comments or attachments for each question.
 
### Model Risks
 
* Black Box Risk:
  * Has the model been approximated by another to provide Global Interpretability? - Yes/No
  * Have Local Interpretability measures been produced for specific important examples? - Yes/No
* Overfitting:
  * Has regularization penalized over-parameterization? - Yes/No
  * Has hyper-parameter tuning and re-sampling prevented generalization errors from
significantly exceeding those on training/validation datasets? - Yes/No
* Model Drift:
  * Is the model automatically, dynamically re-trained? - Yes/No
  * If so, Is a sufficient Adjunct to the Performance Monitoring Plan in-place to guard against
release of a model with undetected large drift? - Yes/No
* Challenges in Calibration and Feedback:
  * Is additional data accumulated for supervised learning? - Yes/No
  * If so, will the initial use of this AI/ML model affect the interpretation of the new labels? - Yes/No
* Potential Biases:
  * Has data used in training has been evaluated for bias and purged of such if needed? - Yes/No
  * Have the algorithms for training the model been identified as highly-prone to producing
biased results? - Yes/No
* Misuse due to lack of Understanding or Misalignment:
  * Have the users of the AI/ML model been well-trained on how to understand and - Yes/No
appropriately use the results? - Yes/No
  * Has the model suitability for this proposed Usage been evaluated and confirmed? - Yes/No
* Heightened Vendor Model Risks:
  * Have vendors provided sufficient information about the model and the data used in its training
to ensure transparency? - Yes/No
  *  Who is accountable for heightened vendor model risks in procuring this model? - Text with name(s)
 
### Data Management
 
* Data Accuracy:
  * Have categorical variables in the AI/ML model been manually labelled? - Yes/No
  * Is accuracy of data monitored at each stage of use? - Yes/No
  * Is there a remediation process for ensuring data issues are resolved? - Yes/No
* Quality:
  * Who are the qualified individuals responsible for data ownership and management? Text with name(s)
  * Has clear accountability been established within processes to address data quality? - Yes/No
* Use of Sensitive Information
  * Is sensitive information used in the AI/ML model? - Yes/No
* Appropriateness and Suitability
  * Was there a documented review confirming the
appropriateness and suitability of the data used in the AI/ML model? - Yes/No
* Bias in Data Selection and Processing
  * Has the data been screened for over-or under-
representation and proxies that could result in bias? - Yes/No
* Data Security
  * Has access to the data used to re-train or apply the AI/ML model been
secured against internal and external threats which could compromise its integrity?
* Complexity and Storage
  * Does the model require storage of large amounts of data or
rapid access to and processing of complex streams of information? - Yes/No
* Adherence to Data Privacy Regulations
  * Is information about people used in the AI/ML
model? - Yes/No
* Data Lineage:
  * Are all Key Data Elements sourced from an enterprise-sanctioned repository with
contents that adhere to strong data lineage practices for the type of data used
including unstructured image or text data types? - Yes/No
  * Has adequate documentation of usage rights and data permissions been compiled for
each stage of data management? - Yes/No
 
### Technology Risk
 
* Integrating into Infrastructure
  * Does the AI/ML model only require pre-existing elements of
the Technology Infrastructure which have well-served applications with similar needs to this
AI/ML model? - Yes/No
* Technology Obsolescence
  * Have approvals from Enterprise Architecture of the selected
technology been obtained to guard against rapid obsolescence? - Yes/No
* Scalability
  * Is the infrastructure to support data storage and computing power necessary to
meet operational and business needs available at the initial scale and sufficiently scalable to
meet likely future needs? - Yes/No
* Potential Performance Issues:
  * Has testing of the in-house or third-party AI/ML tools, applications, and systems to assess
integrity, security, and business resiliency been sufficient to identify any potential significant
performance issues? - Yes/No
  * Do technology change management practices and procedures prevent emergence of future
potential performance issues as the AI/ML technology evolves? - Yes/No
 
### Cybersecurity (Information Security)
 
* Data Theft
  * Is only publicly available data is used in the AI/ML application? - Yes/No
* Adversarial Attacks:
  * Does the AI/ML model ingest external data during its application? - Yes/No
  * Does the AI/ML model does require real-time, rapid availability? - Yes/No
* Infrastructure and System Security:
  * Is the AI/ML hosted in Cloud infrastructure? - Yes/No
  * If so, does the Cloud environment meets Fannie Mae security requirements? - Yes/No
  * Are open-source software or models used? - Yes/No
  * If so, were they provisioned in adherence to open-source governance requirements? - Yes/No
* Data Poisoning
  * Is the lineage of the data used in training the model sufficiently clear to
reduce risks of data poisoning?
 
### Business Resiliency
 
* Downstream Business Processes:
  * Do any downstream business processes depend on successful operation of this AI/ML
capability?
  * Are any dependent downstream business processes protected by adequate business
continuity and incident response plans which have been adapted to this AI/ML context
including by introducing manual override functions if the AI/ML starts to skew results? - Yes/No
* Downstream AI/ML systems:
  * Do any downstream AI/ML systems depend on successful operation of this AI/ML capability? - Yes/No
  * Do any dependent AI/ML systems have workarounds to prevent data dependencies and other
forms of interconnectivity from severely disrupting their operability? - Yes/No
 
### Third-Party Risk
 
* Third-party provided products and services with embedded AI/ML:
  * Is this an ancillary AI/ML usage in the sense that the AI/ML component of the third-party
provided product or service is embedded within an application with an ability to fulfill its
primary purpose even if the AI/ML component is not used? - Yes/No
  * Do contractual requirements with third-party providers of AI/ML models and data ensure
transparency and accountability with use? - Yes/No
* Third-party cloud providers hosting AI/ML platforms:
  * Is a third-party cloud provider hosting this AI/ML platform? - Yes/No
  * Is resiliency against outage of a single third-party cloud provider environment provided by
hosting arrangements? - Yes/No
 
### Compliance Risks
 
* Consumer Protection
  * Does the AI/ML usage affect consumers?
* Fair Lending
  * Is the AI/ML used in lending activities?
* Privacy
  * Is any information about people used in the AI/ML application?
* Employment Discrimination
  * Does the AI/ML usage affect employment outcomes?
* Personal Data:
  * Is personally-identifiable information collected or used in this AI/ML application? - Yes/No
  * If personally-identifiable information is collected or used in this AI/ML application, is there
sufficient anonymization, securing consent to use, and maintaining a record of how data is used,
accessed, and stored? - Yes/No
