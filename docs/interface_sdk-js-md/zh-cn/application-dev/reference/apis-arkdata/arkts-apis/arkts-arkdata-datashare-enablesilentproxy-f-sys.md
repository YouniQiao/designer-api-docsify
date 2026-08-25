# enableSilentProxy（系统接口）

## 导入模块

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## enableSilentProxy

```TypeScript
function enableSilentProxy(context: Context, uri?: string): Promise<void>
```

开启静默访问。使用Promise异步回调。使用规则：  
- 数据提供方调用此接口，来开启静默访问功能。  
- 此接口设置的开启结果在校验的时候是搭配data_share_config.json文件中isSilentProxyEnable字段进行工作的。支持的配置可参考  
[data_share_config.json配置](../../../database/share-data-by-datashareextensionability-sys.md)。  
- 此接口生效在调用datashareHelper相关接口过程中，如果此接口有开启过相关uri，那么会按照此接口的配置来开启静默访问。如果此接口未调用过，则会读取data_share_config.json中的配置来校验  
Datashare的开启状态。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| uri | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700011](../errorcode-datashare.md#15700011-uri不存在) |
