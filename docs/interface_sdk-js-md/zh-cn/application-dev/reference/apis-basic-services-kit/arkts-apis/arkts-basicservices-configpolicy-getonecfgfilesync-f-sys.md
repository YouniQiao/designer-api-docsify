# getOneCfgFileSync（系统接口）

## 导入模块

```TypeScript
import { configPolicy } from 'kits/@kit.BasicServicesKit';
```

## getOneCfgFileSync

```TypeScript
function getOneCfgFileSync(relPath: string, followMode?: FollowXMode, extra?: string): string
```

根据提供的跟随模式，获取指定文件名优先级最高的配置文件路径。

**起始版本：** 11

**系统能力：** SystemCapability.Customization.ConfigPolicy

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| relPath | string | 是 |
| followMode | [FollowXMode](arkts-basicservices-configpolicy-followxmode-e-sys.md) | 否 |
| extra | string | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
