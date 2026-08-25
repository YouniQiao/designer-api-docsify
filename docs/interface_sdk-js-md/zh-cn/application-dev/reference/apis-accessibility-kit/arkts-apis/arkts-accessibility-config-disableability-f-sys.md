# disableAbility（系统接口）

## 导入模块

```TypeScript
import { config } from 'kits/@kit.AccessibilityKit';
```

## disableAbility

```TypeScript
function disableAbility(name: string): Promise<void>
```

关闭辅助扩展，需与[config.enableAbility](arkts-accessibility-config-enableability-f-sys.md)或 [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md)配对使用。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9300001](../errorcode-accessibility.md#9300001-输入无效的包名称或者ability名称) |


## disableAbility

```TypeScript
function disableAbility(name: string, callback: AsyncCallback<void>): void
```

关闭辅助扩展，需与[config.enableAbility](arkts-accessibility-config-enableability-f-sys.md)或 [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md)配对使用。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9300001](../errorcode-accessibility.md#9300001-输入无效的包名称或者ability名称) |
