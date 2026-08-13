# enableAbility（系统接口）

## enableAbility

```TypeScript
function enableAbility(name: string, capability: Array<accessibility.Capability>): Promise<void>
```

启用辅助扩展。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

<!--Device-config-function enableAbility(name: string, capability: Array<accessibility.Capability>): Promise<void>--><!--Device-config-function enableAbility(name: string, capability: Array<accessibility.Capability>): Promise<void>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| capability | Array & lt;accessibility.Capability & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9300001](../errorcode-accessibility.md#9300001-输入无效的包名称或者ability名称) |
| [9300002](../errorcode-accessibility.md#9300002-目标ability已启用) |

## 示例

```TypeScript
import { accessibility, config } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let name: string = 'com.ohos.example/axExtension';
let capability: accessibility.Capability[] = ['retrieve'];

config.enableAbility(name, capability).then(() => {
  console.info(`Succeeded in enabling ability, name is ${name}, capability is ${capability}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to enable ability. Code: ${err.code}, message: ${err.message}`);
});
```


## enableAbility

```TypeScript
function enableAbility(
    name: string,
    capability: Array<accessibility.Capability>,
    callback: AsyncCallback<void>
  ): void
```

启用辅助扩展，使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

<!--Device-config-function enableAbility(    name: string,    capability: Array<accessibility.Capability>,    callback: AsyncCallback<void>  ): void--><!--Device-config-function enableAbility(    name: string,    capability: Array<accessibility.Capability>,    callback: AsyncCallback<void>  ): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| capability | Array & lt;accessibility.Capability & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9300001](../errorcode-accessibility.md#9300001-输入无效的包名称或者ability名称) |
| [9300002](../errorcode-accessibility.md#9300002-目标ability已启用) |

## 示例

```TypeScript
import { accessibility, config } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let name: string = 'com.ohos.example/axExtension';
let capability: accessibility.Capability[] = ['retrieve'];

config.enableAbility(name, capability, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to enable ability. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in enabling ability, name is ${name}, capability is ${capability}`); 
});
```
