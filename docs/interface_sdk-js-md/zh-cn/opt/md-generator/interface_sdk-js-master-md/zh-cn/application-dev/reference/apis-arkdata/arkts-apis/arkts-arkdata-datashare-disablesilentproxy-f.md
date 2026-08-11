# disableSilentProxy

## disableSilentProxy

```TypeScript
function disableSilentProxy(context: Context, uri?: string): Promise<void>
```

关闭静默访问。使用Promise异步回调。

使用规则：

- 数据提供方调用此接口，来关闭静默访问功能。  
- 此接口设置的关闭结果在校验的时候是搭配data_share_config.json文件中isSilentProxyEnable字段进行工作的。支持的配置可参考  
[data_share_config.json配置](../../../database/share-data-by-datashareextensionability-sys.md)。  
- 此接口生效在调用datashareHelper相关接口过程中，如果此接口有关闭过相关uri，那么会按照此接口的配置来关闭静默访问。如果此接口未调用过，则会读取data_share_config.json中的配置来校验  
Datashare的关闭状态。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-dataShare-function disableSilentProxy(context: Context, uri?: string): Promise<void>--><!--Device-dataShare-function disableSilentProxy(context: Context, uri?: string): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| uri | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [15700011](../errorcode-datashare.md#15700011-uri不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let uri = "datashare:///com.acts.datasharetest/entry/DB00/TBL00?Proxy=true";
    let context = this.context;
    dataShare.disableSilentProxy(context, uri).then(() => {
      console.info("disableSilentProxy succeed");
    }).catch((err: BusinessError) => {
      console.error(`Failed to disable silent proxy. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```
