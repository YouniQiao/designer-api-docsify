# EnableAlertBeforeBackPageOptions

定义EnableAlertBeforeBackPage选项。

**起始版本：** 6

**废弃版本：** 8

**替代接口：** EnableAlertOptions

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## cancel

```TypeScript
cancel?: (errMsg: string) => void
```

用户选择对话框取消按钮时触发，errMsg表示返回信息。

**类型：** (errMsg: string) => void

**起始版本：** 6

**废弃版本：** 8

**替代接口：** EnableAlertOptions

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## complete

```TypeScript
complete?: () => void
```

当对话框关闭时触发该回调。

**类型：** () => void

**起始版本：** 6

**废弃版本：** 8

**替代接口：** EnableAlertOptions

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message: string
```

询问对话框内容。

**类型：** string

**起始版本：** 6

**废弃版本：** 8

**替代接口：** message

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## success

```TypeScript
success?: (errMsg: string) => void
```

用户选择对话框确认按钮时触发，errMsg表示返回信息。

**类型：** (errMsg: string) => void

**起始版本：** 6

**废弃版本：** 8

**替代接口：** EnableAlertOptions

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

