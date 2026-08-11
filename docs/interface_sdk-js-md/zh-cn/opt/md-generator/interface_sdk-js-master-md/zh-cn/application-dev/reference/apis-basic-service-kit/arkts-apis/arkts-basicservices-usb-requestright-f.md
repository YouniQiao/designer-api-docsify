# requestRight

## requestRight

```TypeScript
function requestRight(deviceName: string): Promise<boolean>
```

请求软件包的临时权限以访问设备。使用Promise异步回调。系统应用默认拥有访问设备权限，无需调用此接口申请。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [@ohos.usbManager:usbManager.requestRight](arkts-basicservices-usbmanager-requestright-f.md#requestright)

<!--Device-usb-function requestRight(deviceName: string): Promise<boolean>--><!--Device-usb-function requestRight(deviceName: string): Promise<boolean>-End-->

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |

## 示例

```TypeScript
let devicesName= "1-1";
usb.requestRight(devicesName).then((ret) => {
  console.info(`requestRight = ${ret}`);
});
```
