# XMPTagType

表示XMP标签类型的枚举。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-image-enum XMPTagType--><!--Device-image-enum XMPTagType-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## UNKNOWN

```TypeScript
UNKNOWN = 0
```

未知类型。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XMPTagType-UNKNOWN = 0--><!--Device-XMPTagType-UNKNOWN = 0-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## STRING

```TypeScript
STRING = 1
```

字符串类型。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XMPTagType-STRING = 1--><!--Device-XMPTagType-STRING = 1-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## UNORDERED_ARRAY

```TypeScript
UNORDERED_ARRAY = 2
```

无序数组类型。序列化时，此类型在XMP元数据中的格式为&lt;rdf:Bag&gt;。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XMPTagType-UNORDERED_ARRAY = 2--><!--Device-XMPTagType-UNORDERED_ARRAY = 2-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## ORDERED_ARRAY

```TypeScript
ORDERED_ARRAY = 3
```

有序数组类型。序列化时，此类型在XMP元数据中的格式为&lt;rdf:Seq&gt;。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XMPTagType-ORDERED_ARRAY = 3--><!--Device-XMPTagType-ORDERED_ARRAY = 3-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## ALTERNATE_ARRAY

```TypeScript
ALTERNATE_ARRAY = 4
```

备选数组类型。序列化时，此类型在XMP元数据中的格式为&lt;rdf:Alt&gt;。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XMPTagType-ALTERNATE_ARRAY = 4--><!--Device-XMPTagType-ALTERNATE_ARRAY = 4-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## ALTERNATE_TEXT

```TypeScript
ALTERNATE_TEXT = 5
```

多语言文本类型。序列化时，此类型为XMP格式的xml:lang限定符组成的备选数组。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XMPTagType-ALTERNATE_TEXT = 5--><!--Device-XMPTagType-ALTERNATE_TEXT = 5-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## STRUCTURE

```TypeScript
STRUCTURE = 6
```

结构体类型。不同于数组元素，结构体字段可以属于不同的命名空间。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XMPTagType-STRUCTURE = 6--><!--Device-XMPTagType-STRUCTURE = 6-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

