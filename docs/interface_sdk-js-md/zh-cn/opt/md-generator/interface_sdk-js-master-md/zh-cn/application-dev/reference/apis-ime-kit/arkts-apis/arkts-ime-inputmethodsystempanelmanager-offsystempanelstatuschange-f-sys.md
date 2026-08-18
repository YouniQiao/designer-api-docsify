# offSystemPanelStatusChange（系统接口）

## 导入模块

```TypeScript
```

## offSystemPanelStatusChange

```TypeScript
function offSystemPanelStatusChange(callback?: Callback<SystemPanelStatus>): void
```

取消订阅系统面板状态改变事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-inputMethodSystemPanelManager-function offSystemPanelStatusChange(callback?: Callback<SystemPanelStatus>): void--><!--Device-inputMethodSystemPanelManager-function offSystemPanelStatusChange(callback?: Callback<SystemPanelStatus>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SystemPanelStatus](arkts-ime-inputmethodsystempanelmanager-systempanelstatus-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
