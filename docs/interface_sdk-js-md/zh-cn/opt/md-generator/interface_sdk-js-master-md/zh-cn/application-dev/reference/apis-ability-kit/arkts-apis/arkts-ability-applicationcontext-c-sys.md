# ApplicationContext

ApplicationContext作为应用上下文，继承自Context，提供了应用生命周期监听、进程管理、应用环境设置等应用级别的管控能力。 > **说明：** > > 本模块接口仅可在Stage模型下使用。

**继承/实现关系：** ApplicationContext extends Context

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare class ApplicationContext--><!--Device-unnamed-declare class ApplicationContext-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## preloadUIExtensionAbility

```TypeScript
preloadUIExtensionAbility(want: Want): Promise<void>
```

Preload UIExtensionAbility.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.PRELOAD_UI_EXTENSION_ABILITY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ApplicationContext-preloadUIExtensionAbility(want: Want): Promise<void>--><!--Device-ApplicationContext-preloadUIExtensionAbility(want: Want): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## 示例

```TypeScript
import { UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate() {
    // 构造预加载UIExtensionAbility的want参数
    let want: Want = {
      bundleName: 'com.ohos.uiextensionprovider',
      abilityName: 'UIExtensionProvider',
      moduleName: 'entry',
      parameters: {
        // 与UIExtensionAbility在module.json5中"type"字段配置一致
        'ability.want.params.uiExtensionType': 'sys/commonUI'
      }
    };
    try {
      // 获取ApplicationContext实例
      let applicationContext = this.context.getApplicationContext();
      // 预加载UIExtensionAbility
      applicationContext.preloadUIExtensionAbility(want)
        .then(() => {
          // 预加载成功处理
          console.info('preloadUIExtensionAbility succeed');
        })
        .catch((err: BusinessError) => {
          // 预加载失败处理
          console.error('preloadUIExtensionAbility failed');
        });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`preloadUIExtensionAbility failed. code: ${code}, msg: ${message}`);
    }
  }
}
```
