# clearPreloadedUIExtensionAbility（系统接口）

## clearPreloadedUIExtensionAbility

```TypeScript
function clearPreloadedUIExtensionAbility(preloadId: number): Promise<void>
```

清除指定的[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#UIExtensionAbility)实例。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.PRELOAD_UI_EXTENSION_ABILITY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-abilityManager-function clearPreloadedUIExtensionAbility(preloadId: int): Promise<void>--><!--Device-abilityManager-function clearPreloadedUIExtensionAbility(preloadId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| preloadId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000003](../errorcode-ability.md#16000003-指定的id不存在) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 通过preloadUIExtensionAbility接口预加载后返回的ID
  let preloadId: number = 1001;
  abilityManager.clearPreloadedUIExtensionAbility(preloadId)
    .then(() => {
      console.info('clearPreloadedUIExtensionAbility success.');
    })
    .catch((err: BusinessError) => {
      console.error(`clearPreloadedUIExtensionAbility fail, err: ${JSON.stringify(err)}`);
    });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`clearPreloadedUIExtensionAbility failed, code is ${code}, message is ${message}`);
}
```
