# component/rating

提供在给定范围内选择评分的组件。
 > **说明：**
 >
 > - 本模块同时支持ArkTS-Dyn、ArkTS-Sta。
 > - 当Rating的父节点有指定宽高时，需为Rating组件指定宽高，或为父节点设置值为true的[clip](../arkts-arkui-component/common-commonmethod-i.md#clip)属性。
 ###### 子组件
 无
 ###### 键盘走焦规格
 | 按键         | 功能描述                        |
 |------------|-----------------------------|
 | Tab        | 组件间切换焦点。                    |
 | 左右方向键   | 评分预览增加/减少（步长为step），不改变实际分值。 |
 | Home       | 移动到第一个星星， 不改变实际分值。          |
 | End        | 移动到最后一个星星， 不改变实际分值。         |
 | Space/Enter | 根据当前评分提交评分结果。               |


## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [Rating](rating-rating-f.md#rating) | Defines Rating Component. |

### 接口

| 名称 | 说明 |
| --- | --- |
| [RatingAttribute](rating-ratingattribute-i.md) |  |
| [RatingConfiguration](rating-ratingconfiguration-i.md) | 开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_。 |
| [RatingOptions](rating-ratingoptions-i.md) | 评分组件的信息。  @since版本号高于内层元素版本号的情况，但这不影响接口的使用。 |
| [StarStyleOptions](rating-starstyleoptions-i.md) | 评分组件选中、未选中以及部分选中的星级样式。  @since版本号高于内层元素版本号的情况，但这不影响接口的使用。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [OnRatingChangeCallback](arkts-arkui-onratingchangecallback-t.md) | 操作评分条的评星变化时触发该回调。 |

