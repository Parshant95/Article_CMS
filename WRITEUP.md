# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

_For **both** a VM or App Service solution for the CMS app:_

- _Analyze costs, scalability, availability, and workflow_
- _Choose the appropriate solution (VM or App Service) for deploying the app_
- _Justify your choice_

### Assess App Changes That Would Change the Deployment Decision

The decision to use Azure App Service was based on the simplicity of deployment, built-in scaling, and minimal infrastructure management required for this Flask-based CMS application. However, if the application requirements changed to include custom operating system dependencies, specialized background services, or low-level system configurations that are not supported by App Service, deploying the application on a Virtual Machine would be more appropriate.

Additionally, if the application required more control over networking configurations, security policies, or installation of custom software packages at the operating system level, a VM would provide the flexibility needed. In such cases, managing the infrastructure directly through a VM would allow full administrative access to configure the environment according to the application's specific needs.

# Deployment Resource Analysis – Article CMS

This project required deploying a Flask-based Content Management System (CMS) that uses Azure SQL Database for storing article data and Azure Blob Storage for storing images. Two possible deployment options were considered: Azure Virtual Machines and Azure App Service.

---

## Option 1: Azure Virtual Machine

### Cost

Azure Virtual Machines operate on a pay-as-you-go pricing model where the user pays for the compute resources, storage, and networking used by the VM. Even when the application is idle, the VM continues running and generating costs unless it is manually stopped. This makes VMs potentially more expensive for smaller applications like this CMS.

### Scalability

Scaling with Virtual Machines is mostly manual. If traffic increases, additional VMs must be created and configured manually, often requiring load balancers and extra infrastructure. This makes scaling more complex compared to managed services.

### Availability

Virtual Machines provide good availability when configured with availability sets or multiple instances across regions. However, this requires manual configuration and management by the developer or system administrator.

### Workflow

Deploying applications on a VM requires manual setup of the server environment. This includes installing dependencies, configuring Python, setting up web servers such as Nginx or Apache, and managing updates through SSH. This workflow requires more infrastructure management and maintenance.

---

## Option 2: Azure App Service

### Cost

Azure App Service offers several pricing tiers, including a free tier (F1) which is sufficient for small projects like this CMS application. Since infrastructure management is handled by Azure, operational costs and management effort are lower compared to running a VM.

### Scalability

Azure App Service supports built-in scaling capabilities. Applications can scale vertically by increasing the pricing tier or horizontally by adding multiple instances. Auto-scaling rules can also be configured based on traffic or resource usage.

### Availability

Azure App Service provides built-in high availability and is managed by Microsoft. It automatically handles load balancing, patching, and infrastructure maintenance, reducing the risk of downtime compared to manually managed VMs.

### Workflow

Deployment with Azure App Service is simpler and more streamlined. Developers can deploy directly from GitHub, Azure DevOps, or local Git repositories. The platform automatically handles environment configuration, runtime setup, and application hosting.

---

## Deployment Choice

For this project, Azure App Service was chosen as the deployment platform. Azure App Service simplifies deployment and management of web applications by handling infrastructure, scaling, and security automatically. Since this CMS application is a lightweight Flask web application, App Service provides a faster and more efficient way to deploy without the complexity of managing a full virtual machine environment.

Additionally, App Service integrates easily with GitHub for continuous deployment, making it easier to update the application and manage the development workflow.

---

## Assess App Changes That Would Change the Decision

If the application required custom operating system configurations, specialized background services, or software that cannot run within the Azure App Service environment, using a Virtual Machine would become a better option. A VM would allow full administrative control over the operating system, enabling installation of custom dependencies or system-level services.

Additionally, if the application needed advanced networking configurations or more control over security policies and infrastructure, a Virtual Machine would provide the flexibility required for those scenarios.
