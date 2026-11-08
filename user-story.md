# User Story Template

**Title:** [Short, descriptive title]

**As a** [type of user],
**I need** [a capability or feature],
**So that** [the business value or benefit].

## Details and Assumptions
- [Document relevant background, constraints, and assumptions.]

## Acceptance Criteria

```gherkin
Given [some initial context]
When [an action is performed]
Then [an expected outcome occurs]
```

---

## Example: Create a Customer Account

**As a** customer service representative,
**I need** to create a new customer account with a name and email address,
**So that** customer information can be managed through the Customer Accounts microservice.

### Details and Assumptions
- The service exposes a REST API for customer account management.
- The request includes the required customer details.
- Invalid requests return an appropriate error response.

### Acceptance Criteria

```gherkin
Given the Customer Accounts microservice is available
When I submit a valid request to create a customer account
Then the service creates the account
And returns the account details with a successful HTTP status
```

```gherkin
Given the Customer Accounts microservice is available
When I submit a request missing required customer information
Then the service rejects the request
And returns an appropriate validation error
```
