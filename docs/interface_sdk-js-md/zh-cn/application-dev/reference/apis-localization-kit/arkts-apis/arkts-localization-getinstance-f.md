# getInstance

## getInstance

```TypeScript
export function getInstance(locale?:string): IndexUtil
```

创建并返回IndexUtil对象。

**起始版本：** 8

**元服务API：** 从API版本12开始，该接口支持在元服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locale | string | 否 | [表示区域ID的字符串](../../../../internationalization/i18n-locale-culture.md#实现原理)，由语言、脚本、国家地区组成。<br>默认值：系统当前区域ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IndexUtil | 根据区域ID创建的IndexUtil对象。 |

