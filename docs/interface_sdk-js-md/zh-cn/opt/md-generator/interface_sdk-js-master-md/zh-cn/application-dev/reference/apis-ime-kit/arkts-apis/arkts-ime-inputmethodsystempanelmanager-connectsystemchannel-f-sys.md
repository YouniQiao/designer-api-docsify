# connectSystemChannel（系统接口）

## connectSystemChannel

```TypeScript
function connectSystemChannel(): Promise<void>
```

连接面板和输入法之间的系统通道。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CONNECT_IME_ABILITY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-inputMethodSystemPanelManager-function connectSystemChannel(): Promise<void>--><!--Device-inputMethodSystemPanelManager-function connectSystemChannel(): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [12800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800026-输入法系统面板错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [12800008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
