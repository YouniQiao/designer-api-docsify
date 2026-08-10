# getSupportedPowerMode

## 导入模块

```TypeScript
import { wifiManagerExt } from 'kits/@kit.ConnectivityKit';
```

## getSupportedPowerMode

```TypeScript
function getSupportedPowerMode(): Promise<Array<PowerMode>>
```

Obtains the supported power Mode.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**需要权限：** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManagerExt-function getSupportedPowerMode(): Promise<Array<PowerMode>>--><!--Device-wifiManagerExt-function getSupportedPowerMode(): Promise<Array<PowerMode>>-End-->

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;PowerMode&gt;&gt; | Returns a list of application PowerMode. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |
| 201 | Permission denied. |


## getSupportedPowerMode

```TypeScript
function getSupportedPowerMode(callback: AsyncCallback<Array<PowerMode>>): void
```

Obtains the supported power Mode.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**需要权限：** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManagerExt-function getSupportedPowerMode(callback: AsyncCallback<Array<PowerMode>>): void--><!--Device-wifiManagerExt-function getSupportedPowerMode(callback: AsyncCallback<Array<PowerMode>>): void-End-->

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;PowerMode&gt;&gt; | 是 | the callback of model. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |
| 201 | Permission denied. |

## 示例

```TypeScript
import { wifiManagerExt } from '@kit.ConnectivityKit';

wifiManagerExt.getSupportedPowerMode((err, data: wifiManagerExt.PowerMode[]) => {
    if (err) {
        console.error("get supported power mode info error: ", err);
        return;
    }
    console.info("get supported power mode info: " + JSON.stringify(data));
});
```

