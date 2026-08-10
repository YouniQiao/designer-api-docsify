# setSlotFlagsByBundle（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## setSlotFlagsByBundle

```TypeScript
function setSlotFlagsByBundle(bundle: BundleOption, slotFlags: long): Promise<void>
```

设定指定应用的通知提醒方式开关。使用Promise异步回调。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function setSlotFlagsByBundle(bundle: BundleOption, slotFlags: long): Promise<void>--><!--Device-notificationManager-function setSlotFlagsByBundle(bundle: BundleOption, slotFlags: long): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md) | 是 | 指定应用的包信息。 |
| slotFlags | ArkTS-Dyn: number  <br>ArkTS-Sta：long | 是 | 通知提醒方式开关标识位。&lt;br&gt;- bit0：铃声提示。0表示关闭，1表示开启。 &lt;br&gt;- bit1：锁屏。0表示关闭，1表示开启。 &lt;br&gt;- bit2：横幅。0表示关闭 ，1表示开启。 &lt;br&gt;- bit3：亮屏。0表示关闭，1表示开启。 &lt;br&gt;- bit4：振动。0表示关闭，1表示开启。 &lt;br&gt;- bit5：状态栏通知图标。0表示关闭，1表示开启。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported.<br>**适用版本：** 18+ |
| 201 | Permission denied. |
| 1600001 | Internal error. |
| 202 | Not system application to call the interface. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 17700001 | The specified bundle name was not found. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bundle: notificationManager.BundleOption = {
    bundle: 'bundleName1',
};

let slotFlags: number = 1;

notificationManager.setSlotFlagsByBundle(bundle, slotFlags).then(() => {
    console.info('setSlotFlagsByBundle success');
}).catch((err: BusinessError) => {
    console.error(`setSlotFlagsByBundle failed, code is ${err.code}, message is ${err.message}`);
});
```

