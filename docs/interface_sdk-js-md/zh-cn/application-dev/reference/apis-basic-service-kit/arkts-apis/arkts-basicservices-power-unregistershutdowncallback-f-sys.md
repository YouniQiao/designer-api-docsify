# unregisterShutdownCallback（系统接口）

## 导入模块

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## unregisterShutdownCallback

```TypeScript
function unregisterShutdownCallback(callback?: Callback<void>): void
```

取消订阅电源关机或重启的回调提醒。使用callback同步回调。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.REBOOT

<!--Device-power-function unregisterShutdownCallback(callback?: Callback<void>): void--><!--Device-power-function unregisterShutdownCallback(callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 | 回调函数，无返回值。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 4900101 | Failed to connect to the service. |

## 示例

```TypeScript
try {
    power.unregisterShutdownCallback(() => {
        console.info('unsubscribe shutdown success.');
    });
    console.info('unregister shutdown callback success.');
} catch (err) {
    console.error(`Failed to unregister shutdown callback. Code: ${err.code}, message: ${err.message}`);
}
```

