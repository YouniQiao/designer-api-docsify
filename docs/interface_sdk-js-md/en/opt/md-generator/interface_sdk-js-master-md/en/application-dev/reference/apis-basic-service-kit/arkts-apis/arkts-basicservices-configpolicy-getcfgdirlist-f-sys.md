# getCfgDirList (System API)

## Modules to Import

```TypeScript
import { configPolicy } from '@kit.BasicServicesKit';
```

## getCfgDirList

```TypeScript
function getCfgDirList(callback: AsyncCallback<Array<string>>): void
```

Obtains a list of configuration level directories, in ascending order of priority. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-configPolicy-function getCfgDirList(callback: AsyncCallback<Array<string>>): void--><!--Device-configPolicy-function getCfgDirList(callback: AsyncCallback<Array<string>>): void-End-->

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## getCfgDirList

```TypeScript
function getCfgDirList(): Promise<Array<string>>
```

Obtains a list of configuration level directories, in ascending order of priority. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-configPolicy-function getCfgDirList(): Promise<Array<string>>--><!--Device-configPolicy-function getCfgDirList(): Promise<Array<string>>-End-->

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |
