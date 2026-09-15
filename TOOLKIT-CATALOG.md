# Mudit Dholakia — fabric toolkit and agent learning catalog

All forks preserve upstream attribution. The original portfolio implementations remain separate. No toolkit code was copied into this portfolio repository.

| Repository | Purpose / first exercise | License | Collection action |
| --- | --- | --- | --- |
| [microsoft/fabric-data-agent-workshop](https://github.com/muditdholakia/fabric-data-agent-workshop) | Lab 1: create and optimize | MIT | Curated fork |
| [microsoft/fabric-samples](https://github.com/muditdholakia/fabric-samples) | docs-samples/data-science/data-agent-sdk/responses-api | MIT | Curated fork |
| [microsoft/fabric-extensibility-toolkit](https://github.com/muditdholakia/fabric-extensibility-toolkit) | Build custom workloads integrated into Fabric; current successor to WDK | MIT | Curated fork |
| [microsoft/fabric-extensibility-toolkit-validator](https://github.com/microsoft/fabric-extensibility-toolkit-validator) | Validate workload packages; latest inspected update December 2025; verify release compatibility | MIT | Reference only |
| [microsoft/fabric-launcher](https://github.com/microsoft/fabric-launcher) | Deploy solution repositories into Fabric notebooks; wraps fabric-cicd | MIT | Reference only / published package |
| [microsoft/fabric-user-data-functions-samples](https://github.com/muditdholakia/fabric-user-data-functions-samples) | Official User data functions snippets; insert into a configured UDF item, not standalone apps | MIT | Curated fork |
| [microsoft/fabric-cicd](https://github.com/microsoft/fabric-cicd) | Supported code-first item deployment | MIT | Reference only / published package |
| [microsoft/semantic-link-labs](https://github.com/muditdholakia/semantic-link-labs) | Semantic-model notebooks and administration; early-access features | MIT | Curated fork |

## Current compatibility and security

- Use supported Microsoft 365 Agents SDK / Agent Framework examples; older TeamsFx paths need migration.
- Fabric data agent query examples should use current Responses/MCP guidance; the older external Assistants-based client is not a recommended starting point.
- Fabric data agent SDK and some Power CAT components are preview-dependent; verify versions and prerequisites.
- The Fabric Tools Workload repository has restrictive pre-release licensing and is not publicly mirrored.
- Fork workflows are disabled. Dependency/secret scans are point-in-time checks; remediate selected examples before execution.
- Do not commit production identifiers, secrets, user conversations, or customer data. Use synthetic inputs and development identities.

## Learning evidence

For each selected example, record architecture, SDK versions, setup, a successful prompt, negative grounding/permission tests, and one operational failure. Implement an original variation here and preserve attribution for adaptations. Do not present upstream agents as original authorship.

References: [Fabric data agent SDK](https://learn.microsoft.com/en-us/fabric/data-science/fabric-data-agent-sdk), [Microsoft agent samples](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/agent-samples).
