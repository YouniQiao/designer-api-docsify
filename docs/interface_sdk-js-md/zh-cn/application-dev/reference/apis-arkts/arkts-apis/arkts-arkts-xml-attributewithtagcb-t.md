# AttributeWithTagCb

```TypeScript
type AttributeWithTagCb = (tagName: string, key: string, value: string) => boolean
```

ParseOptions中attributeWithTagCallbackFunction的回调方法，三个字符串参数都是由XML解析器在解析过程中自动提取的，开发者无法直接自定义这些值。开发者只能在回调函数中通过返回值来决定如何处 理这些已存在的属性。

**起始版本：** 24

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-xml-type AttributeWithTagCb = (tagName: string, key: string, value: string) => boolean--><!--Device-xml-type AttributeWithTagCb = (tagName: string, key: string, value: string) => boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tagName | string | 是 | 标签名称。 |
| key | string | 是 | 属性名称。 |
| value | string | 是 | 属性的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否继续解析标签名称、属性名称及属性的值。true表示继续解析，false表示停止解析。 |

**示例**

```TypeScript
let xmlStr = 
    '<?xml version="1.0" encoding="utf-8"?>' +
    '<column name="Giana"><value integer="1"/></column>' +
    '<column name="category"><value Boolean="true"/></column>' +
    '<column name="day"><orange Boolean="3"/></column>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(xmlStr);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer, 'UTF-8');

let attrWithTag = (tagName: string, key: string, value: string): boolean => {
    if (tagName == "orange") {
        console.info('key: ',key,' value: ',value); // key:  Boolean  value:  3
        arktest.assertEQ(value, '3');
    }
    return true;
}

let options: xml.ParseOptions = {
    supportDoctype: true,
    ignoreNameSpace: true,
    attributeWithTagCallbackFunction:attrWithTag
};
that.parseXml(options);
```

