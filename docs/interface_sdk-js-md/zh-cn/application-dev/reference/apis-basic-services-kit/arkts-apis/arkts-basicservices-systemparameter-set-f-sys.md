# set（系统接口）

## 导入模块

```TypeScript
import { systemParameter } from 'kits/@kit.BasicServicesKit';
```

## set

```TypeScript
function set(key: string, value: string, callback: AsyncCallback<void>): void
```

设置系统参数key对应的值，使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** set

**系统能力：** SystemCapability.Startup.SystemInfo

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14700102](../errorcode-system-parameterV9.md#14700102-系统参数值无效) |
| [14700103](../errorcode-device-info.md#14700103-操作因权限被拒绝) |
| [14700104](../errorcode-system-parameterV9.md#14700104-系统内部错误包括内存不足死锁等) |


## set

```TypeScript
function set(key: string, value: string): Promise<void>
```

设置系统参数key对应的值，使用Promise异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** set

**系统能力：** SystemCapability.Startup.SystemInfo

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14700102](../errorcode-system-parameterV9.md#14700102-系统参数值无效) |
| [14700103](../errorcode-device-info.md#14700103-操作因权限被拒绝) |
| [14700104](../errorcode-system-parameterV9.md#14700104-系统内部错误包括内存不足死锁等) |
