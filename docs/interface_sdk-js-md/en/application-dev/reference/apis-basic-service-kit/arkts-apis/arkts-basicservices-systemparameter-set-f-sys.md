# set (System API)

## Modules to Import

```TypeScript
import { systemParameter } from '@kit.BasicServicesKit';
```

## set

```TypeScript
function set(key: string, value: string, callback: AsyncCallback<void>): void
```

Sets a value for the specified key. This API uses an asynchronous callback to return the result.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** set

<!--Device-systemParameter-function set(key: string, value: string, callback: AsyncCallback<void>): void--><!--Device-systemParameter-function set(key: string, value: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Startup.SystemInfo

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Target key. |
| value | string | Yes | Value to set. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |


## set

```TypeScript
function set(key: string, value: string): Promise<void>
```

Sets a value for the specified key. This API uses a promise to return the result.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** set

<!--Device-systemParameter-function set(key: string, value: string): Promise<void>--><!--Device-systemParameter-function set(key: string, value: string): Promise<void>-End-->

**System capability:** SystemCapability.Startup.SystemInfo

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Target key. |
| value | string | Yes | Value to set. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the execution result. |

