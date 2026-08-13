# sendPrivateCommand（系统接口）

## sendPrivateCommand

```TypeScript
function sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>
```

发送私有命令。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-inputMethodSystemPanelManager-function sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>--><!--Device-inputMethodSystemPanelManager-function sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| commandData | Record & lt;string, CommandDataType & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800026](../errorcode-inputmethod-framework.md#12800026-输入法系统面板错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
