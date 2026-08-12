# rating

提供在给定范围内选择评分的组件。
 > **说明：**
 >
 > - 本模块同时支持ArkTS-Dyn、ArkTS-Sta。
 > - 当Rating的父节点有指定宽高时，需为Rating组件指定宽高，或为父节点设置值为true的[clip](CommonMethod#clip(clip: Optional<boolean>))属性。
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
| [Rating](arkts-arkui-rating-rating-f.md#rating) | Defines Rating Component. |

### 接口

| 名称 | 说明 |
| --- | --- |
| [RatingAttribute](arkts-arkui-rating-ratingattribute-i.md) |  |
| [RatingConfiguration](arkts-arkui-rating-ratingconfiguration-i.md) | 开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](CommonConfiguration)。 |
| [RatingOptions](arkts-arkui-rating-ratingoptions-i.md) | 评分组件的信息。  @since版本号高于内层元素版本号的情况，但这不影响接口的使用。 |
| [StarStyleOptions](arkts-arkui-rating-starstyleoptions-i.md) | 评分组件选中、未选中以及部分选中的星级样式。  @since版本号高于内层元素版本号的情况，但这不影响接口的使用。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [OnRatingChangeCallback](arkts-arkui-onratingchangecallback-t.md) | 操作评分条的评星变化时触发该回调。 |

