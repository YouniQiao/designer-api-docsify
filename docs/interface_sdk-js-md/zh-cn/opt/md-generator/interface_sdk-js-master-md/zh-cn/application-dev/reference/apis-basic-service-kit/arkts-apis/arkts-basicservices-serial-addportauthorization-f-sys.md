# addPortAuthorization（系统接口）

## addPortAuthorization

```TypeScript
function addPortAuthorization(tokenId: string, deviceId: string): Promise<void>
```

添加应用访问串口端口的权限仅面向串口授权弹窗系统应用开放

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-serial-function addPortAuthorization(tokenId: string, deviceId: string): Promise<void>--><!--Device-serial-function addPortAuthorization(tokenId: string, deviceId: string): Promise<void>-End-->

**系统能力：** SystemCapability.BusManager.Serial

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenId | string | 是 |
| deviceId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [35700001](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700001-服务异常) |
| [35700002](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700002-参数错误) |
| [35700008](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700008-权限被拒绝) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
