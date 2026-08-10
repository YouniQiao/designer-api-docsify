# getOAID

## Modules to Import

```TypeScript
import { identifier } from 'kits/@kit.AdsKit';
```

## getOAID

```TypeScript
function getOAID(callback: AsyncCallback<string>): void
```

获取开放匿名设备标识符（OAID）。使用callback异步回调。

> **说明：**
> 
> 设置项“跨应用关联访问权限”在HarmonyOS NEXT Developer Beta5及更早版本名称为“应用跟踪访问权限”。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.APP_TRACKING_CONSENT

<!--Device-identifier-function getOAID(callback: AsyncCallback<string>): void--><!--Device-identifier-function getOAID(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Advertising.OAID

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数，返回开放匿名设备标识符（OAID）。 1.如应用已配置ohos.permission.APP_TRACKING_CONSENT权限，且“跨应用关联访问权限”为“允许”，则返回OAID。 2.如应用已配置ohos.permission.APP_TRACKING_CONSENT权限，且“跨应用关联访问权限”为“禁止”，则返回 00000000-0000-0000-0000-000000000000。 3.如应用未配置ohos.permission.APP_TRACKING_CONSENT权限，则返回00000000-0000-0000-0000-000000000000。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17300001 | System internal error. |

## Examples

```TypeScript
import { identifier } from '@kit.AdsKit';
import { BusinessError } from '@kit.BasicServicesKit';

identifier.getOAID((err: BusinessError, data: string) => {
  if (err.code) {
    return;
  }
  const oaid: string = data;
});
```


## getOAID

```TypeScript
function getOAID(): Promise<string>
```

获取开放匿名设备标识符（OAID）。使用Promise异步回调。

> **说明：**
> 
> 设置项“跨应用关联访问权限”在HarmonyOS NEXT Developer Beta5及更早版本名称为“应用跟踪访问权限”。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.APP_TRACKING_CONSENT

<!--Device-identifier-function getOAID(): Promise<string>--><!--Device-identifier-function getOAID(): Promise<string>-End-->

**System capability:** SystemCapability.Advertising.OAID

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回开放匿名设备标识符（OAID）。 1.如应用已配置ohos.permission.APP_TRACKING_CONSENT权限，且跨应用关联访问权限为“允许”，则返回OAID。 2.如应用已配置ohos.permission.APP_TRACKING_CONSENT权限，且跨应用关联访问权限为“禁止”，则返回 00000000-0000-0000-0000-000000000000。 3.如应用未配置ohos.permission.APP_TRACKING_CONSENT权限，则返回00000000-0000-0000-0000-000000000000。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17300001 | System internal error. |

## Examples

```TypeScript
import { identifier } from '@kit.AdsKit';

identifier.getOAID().then((data: string) => {
  const oaid: string = data;
});
```

