# Search

The **Search** component provides an area for users to enter search queries. > **NOTE** > > This component supports plain text only. For rich text, use the RichEditor component.

## Child Components Not supported

## Search

```TypeScript
Search(options?: SearchOptions)
```

Defines the constructor of Search.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SearchInterface-(options?: SearchOptions): SearchAttribute--><!--Device-SearchInterface-(options?: SearchOptions): SearchAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SearchOptions](arkts-arkui-searchoptions-i.md) | No | Initialization options of the **Search** component. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [CancelButtonOptions](arkts-arkui-cancelbuttonoptions-i.md) | Defines the CancelButton options. |
| [IconOptions](arkts-arkui-iconoptions-i.md) | Defines the icon options. |
| [SearchButtonOptions](arkts-arkui-searchbuttonoptions-i.md) | Defines the SearchButton options. |
| [SearchOptions](arkts-arkui-searchoptions-i.md) | Describes the initialization options of the **Search** component. &gt; **NOTE：**&gt; &gt; To standardize anonymous object definitions, the element definitions here have been revised in API version 18. &gt; While historical version information is preserved for anonymous objects, there may be cases where the outer element &gt; 's @since version number is higher than inner elements'. This does not affect interface usability. |

### Types

| Name | Description |
| --- | --- |
| [SearchSubmitCallback](arkts-arkui-searchsubmitcallback-t.md) | Called when the search icon, search button, or soft keyboard search button is clicked. |

### Enums

| Name | Description |
| --- | --- |
| [CancelButtonStyle](arkts-arkui-cancelbuttonstyle-e.md) | Enum for the style of cancel button. |
| [SearchType](arkts-arkui-searchtype-e.md) | Enumerates the text input types of a search box. |

