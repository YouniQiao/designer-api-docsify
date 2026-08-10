# isScreenOn

## Modules to Import

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## isScreenOn

```TypeScript
function isScreenOn(callback: AsyncCallback<boolean>): void
```

检测当前设备的亮灭屏状态。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [power.isActive](arkts-basicservices-power-isactive-f.md#isactive)

<!--Device-power-function isScreenOn(callback: AsyncCallback<boolean>): void--><!--Device-power-function isScreenOn(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 回调函数。当检测成功，err为undefined，data为获取到的亮灭屏状态，返回true表示亮屏，返回false表示灭屏；否则为错误对象 。 |

## Examples

```TypeScript
power.isScreenOn((err: Error, data: boolean) => {
    if (typeof err === 'undefined') {
        console.info('screen on status is ' + data);
    } else {
        console.error('check screen status failed, err: ' + err);
    }
})
```


## isScreenOn

```TypeScript
function isScreenOn(): Promise<boolean>
```

检测当前设备的亮灭屏状态。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [power.isActive](arkts-basicservices-power-isactive-f.md#isactive)

<!--Device-power-function isScreenOn(): Promise<boolean>--><!--Device-power-function isScreenOn(): Promise<boolean>-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示亮屏；返回false表示灭屏。 |

## Examples

```TypeScript
power.isScreenOn()
.then((data: boolean) => {
    console.info('screen on status is ' + data);
})
.catch((err: Error) => {
    console.error('check screen status failed, err: ' + err);
})
```

