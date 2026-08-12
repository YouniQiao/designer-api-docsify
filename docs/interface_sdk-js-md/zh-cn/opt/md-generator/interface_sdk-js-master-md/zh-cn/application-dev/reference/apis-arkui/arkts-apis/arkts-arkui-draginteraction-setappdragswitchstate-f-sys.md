# setAppDragSwitchState（系统接口）

## setAppDragSwitchState

```TypeScript
function setAppDragSwitchState(enabled: boolean, bundleName: string): void
```

控制统一拖拽适配应用开关。

**起始版本：** 18

<!--Device-dragInteraction-function setAppDragSwitchState(enabled: boolean, bundleName: string): void--><!--Device-dragInteraction-function setAppDragSwitchState(enabled: boolean, bundleName: string): void-End-->

**系统能力：** SystemCapability.Msdp.DeviceStatus.Drag

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |
| bundleName | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
