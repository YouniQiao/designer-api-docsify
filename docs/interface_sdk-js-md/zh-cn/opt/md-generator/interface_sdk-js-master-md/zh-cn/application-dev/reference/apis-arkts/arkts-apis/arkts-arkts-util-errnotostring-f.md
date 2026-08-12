# errnoToString

## errnoToString

```TypeScript
function errnoToString(errno: number): string
```

获取系统错误码对应的详细信息。适用于系统调用出错时将数字错误码转换为可读的描述信息，便于开发者快速定位和排查系统级错误，常用于错误日志记录和错误提示显示。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-util-function errnoToString(errno: number): string--><!--Device-util-function errnoToString(errno: number): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [errno](../../apis-universal-keystore-kit/arkts-apis/arkts-universalkeystore-huksexternalcrypto-huksexternalerrorinfo-i.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## 示例

```TypeScript
let errnum = -1; // -1 : a system error number
let result = util.errnoToString(errnum);
console.info("result = " + result);
// 输出结果：result = operation not permitted
```
