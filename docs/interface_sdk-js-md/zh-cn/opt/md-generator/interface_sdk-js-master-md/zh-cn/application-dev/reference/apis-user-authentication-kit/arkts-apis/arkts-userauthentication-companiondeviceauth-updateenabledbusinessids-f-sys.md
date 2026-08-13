# updateEnabledBusinessIds（系统接口）

## updateEnabledBusinessIds

```TypeScript
function updateEnabledBusinessIds(templateId: Uint8Array, enabledBusinessIds: number[]): Promise<void>
```

更新指定伴随设备模板支持的业务范围。用于修改已注册模板的启用业务ID列表，从而控制该模板可参与的业务场景。使用Promise异步回调。 生效机制：更新立即生效，下一次认证按新的业务范围判断，无需重启应用或重新认证。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.USE_USER_IDM

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-companionDeviceAuth-function updateEnabledBusinessIds(templateId: Uint8Array, enabledBusinessIds: int[]): Promise<void>--><!--Device-companionDeviceAuth-function updateEnabledBusinessIds(templateId: Uint8Array, enabledBusinessIds: int[]): Promise<void>-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| templateId | Uint8Array | 是 |
| [enabledBusinessIds](arkts-userauthentication-companiondeviceauth-templatestatus-i-sys.md) | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [32600001](../errorcode-useriam.md#32600001-系统服务工作异常) |
| [32600003](../errorcode-useriam.md#32600003-业务id无效) |
| [32600002](../errorcode-useriam.md#32600002-模板未找到) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const templateId = new Uint8Array([1, 2, 3]);
companionDeviceAuth.updateEnabledBusinessIds(templateId, [companionDeviceAuth.BusinessId.DEFAULT])
  .then(() => {
    console.info('business scope updated');
  })
  .catch((err: BusinessError) => {
    console.error(`error has been captured. Code: ${err.code}, message: ${err.message}`);
  })
```
