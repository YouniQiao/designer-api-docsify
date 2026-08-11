# getSync（系统接口）

## getSync

```TypeScript
function getSync(key: string, def?: string): string
```

获取系统参数key对应的值。

> **说明：**
> 
> getSync和get方法都用于获取系统参数值：
> - getSync：同步方法，直接返回系统参数值，适用于简单同步场景。
> - get：异步方法，使用callback或Promise异步返回结果，适用于需要异步处理的场景。
> 
> 开发者应根据具体场景选择合适的方法。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** ohos.systemParameterEnhance.getSync

<!--Device-systemParameter-function getSync(key: string, def?: string): string--><!--Device-systemParameter-function getSync(key: string, def?: string): string-End-->

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
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [14700102](../../apis-basic-services-kit/errorcode-system-parameterV9.md#14700102-系统参数值无效) |
| [14700103](../../apis-basic-services-kit/errorcode-device-info.md#14700103-操作因权限被拒绝) |
| [14700104](../../apis-basic-services-kit/errorcode-system-parameterV9.md#14700104-系统内部错误包括内存不足死锁等) |

## 示例

```TypeScript
try {
  let info: string = systemParameter.getSync('const.ohos.apiversion');
  console.info(JSON.stringify(info));
} catch (e) {
  console.error('getSync unexpected error: ' + e);
}
```
