# clearUpApplicationData (System API)

## clearUpApplicationData

```TypeScript
function clearUpApplicationData(bundleName: string): Promise<void>
```

通过Bundle名称清除应用数据。使用Promise异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.app.ability.appManager/appManager#clearUpApplicationData

**Required permissions:** ohos.permission.CLEAN_APPLICATION_DATA

<!--Device-appManager-function clearUpApplicationData(bundleName: string): Promise<void>--><!--Device-appManager-function clearUpApplicationData(bundleName: string): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 表示Bundle名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

## Examples

```TypeScript
import appManager from '@ohos.application.appManager';
import { BusinessError } from '@ohos.base';

let bundleName = 'bundleName';
appManager.clearUpApplicationData(bundleName)
  .then((data) => {
    console.info(`ClearUpApplicationData success, data: ${JSON.stringify(data)}.`);
  })
  .catch((err: BusinessError) => {
    console.error(`ClearUpApplicationData failed, error code: ${err.code}, error msg: ${err.message}.`);
  });
```


## clearUpApplicationData

```TypeScript
function clearUpApplicationData(bundleName: string, callback: AsyncCallback<void>)
```

通过Bundle名称清除应用数据。使用callback异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.app.ability.appManager/appManager#clearUpApplicationData

**Required permissions:** ohos.permission.CLEAN_APPLICATION_DATA

<!--Device-appManager-function clearUpApplicationData(bundleName: string, callback: AsyncCallback<void>)--><!--Device-appManager-function clearUpApplicationData(bundleName: string, callback: AsyncCallback<void>)-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 表示Bundle名称。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当通过Bundle名称清除应用数据成功，err为undefined，否则为错误对象。 |

## Examples

```TypeScript
import appManager from '@ohos.application.appManager';
import { BusinessError } from '@ohos.base';

let bundleName = 'bundleName';

function clearUpApplicationDataCallback(err: BusinessError, data: void) {
  if (err) {
    console.error(`ClearUpApplicationDataCallback failed, error code: ${err.code}, error msg: ${err.message}.`);
  } else {
    console.info(`ClearUpApplicationDataCallback success, data: ${JSON.stringify(data)}.`);
  }
}

appManager.clearUpApplicationData(bundleName, clearUpApplicationDataCallback);
```

