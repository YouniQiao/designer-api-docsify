# getSync（系统接口）

## 导入模块

```TypeScript
import { systemParameterEnhance } from 'kits/@kit.BasicServicesKit';
```

## getSync

```TypeScript
function getSync(key: string, def?: string): string
```

获取系统参数key对应的值。

> **说明：**&gt;
> getSync和get方法都用于获取系统参数值：
> - getSync：同步方法，直接返回系统参数值，适用于简单同步场景。
> - get：异步方法，使用callback或Promise异步返回结果，适用于需要异步处理的场景。&gt;
> 开发者应根据具体场景选择合适的方法。

**起始版本：** 9

**系统能力：** SystemCapability.Startup.SystemInfo

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| def | string | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14700101](../errorcode-system-parameterV9.md#14700101-系统参数查找失败) |
| [14700103](../errorcode-device-info.md#14700103-操作因权限被拒绝) |
| [14700104](../errorcode-system-parameterV9.md#14700104-系统内部错误包括内存不足死锁等) |
