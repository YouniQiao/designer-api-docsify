# get (System API)

## Modules to Import

```TypeScript
import { systemParameter } from 'systemParameter';
```

## get

```TypeScript
function get(key: string, callback: AsyncCallback<string>): void
```

Obtains a value of the specified key. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** get

<!--Device-systemParameter-function get(key: string, callback: AsyncCallback<string>): void--><!--Device-systemParameter-function get(key: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Startup.SystemInfo

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Key to be queried. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Callback used to return the result. |


## get

```TypeScript
function get(key: string, def: string, callback: AsyncCallback<string>): void
```

Obtains a value of the specified key. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** get

<!--Device-systemParameter-function get(key: string, def: string, callback: AsyncCallback<string>): void--><!--Device-systemParameter-function get(key: string, def: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Startup.SystemInfo

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Key to be queried. |
| def | string | Yes | Default value. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Callback used to return the result. |


## get

```TypeScript
function get(key: string, def?: string): Promise<string>
```

Obtains a value of the specified key. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** get

<!--Device-systemParameter-function get(key: string, def?: string): Promise<string>--><!--Device-systemParameter-function get(key: string, def?: string): Promise<string>-End-->

**System capability:** SystemCapability.Startup.SystemInfo

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Key to be queried. |
| def | string | No | Default value of the system parameter.<br> It works only when the system parameter does not exist.<br> The value can be **undefined** or any custom value. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the execution result. |

