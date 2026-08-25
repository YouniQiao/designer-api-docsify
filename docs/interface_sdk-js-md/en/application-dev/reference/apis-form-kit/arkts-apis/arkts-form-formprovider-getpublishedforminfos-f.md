# getPublishedFormInfos

## Modules to Import

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## getPublishedFormInfos

```TypeScript
function getPublishedFormInfos(): Promise<Array<formInfo.FormInfo>>
```

Obtains the information of all widgets that have been added to the home screen on the device. This API uses a promise to return the result.

> **NOTE：**&gt;
> This field is supported since API version 18 and deprecated since API version 20. You are advised to use
> [getPublishedRunningFormInfos](arkts-form-formprovider-getpublishedrunningforminfos-f.md) instead.

**Since:** 18

**Deprecated since:** 20

**Substitutes:** [getPublishedRunningFormInfos](arkts-form-formprovider-getpublishedrunningforminfos-f.md)

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Ability.Form

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;formInfo.FormInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
