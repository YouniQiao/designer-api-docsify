# setWantAgentMultithreading (System API)

## Modules to Import

```TypeScript
import { WantAgent } from '@kit.AbilityKit';
```

## setWantAgentMultithreading

```TypeScript
function setWantAgentMultithreading(isMultithreadingSupported: boolean) : void
```

Enables or disables the WantAgent multithreading feature.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

<!--Device-wantAgent-function setWantAgentMultithreading(isMultithreadingSupported: boolean) : void--><!--Device-wantAgent-function setWantAgentMultithreading(isMultithreadingSupported: boolean) : void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isMultithreadingSupported | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
