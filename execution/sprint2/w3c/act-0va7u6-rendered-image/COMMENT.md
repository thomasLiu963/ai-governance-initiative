# Comment for act-rules/act-rules.github.io issue 2408

Not posted. One comment on the existing issue. The replacement glossary file is in this directory. Do not open a pull request until the comment is approved, and do not open the pull request in the same step as the comment unless the approval says to.

The person who posts this is responsible for every sentence. An LLM drafted the replacement from the glossary, the rule, and HTML's definition of image source. Keep the disclosure line.

## Body

```markdown
The definition still points only at HTML's image-source list. That list is defined for `img` (and `link`). Rule 0va7u6 already has passed and failed examples for `input type="image"`, `object`, an `svg` `image`, and `background-image`. Under the current sentence those examples are not rendered image resources, so the rule does not apply to them.

`pages/glossary/rendered-image-resource.md` on `develop` `50d2bede1ee705be6840d06f356a6ae2fd94cb2c` says a rendered image resource is a resource with visible pixels "specified in the list of image sources of an embedded image." `embedded-image` already lists the five cases separately.

Proposed replacement, keeping the `img` case on the HTML image-source list and naming the resource the other four cases actually use:

> A rendered image resource in a web page is any resource with visible pixels presented by an embedded image, as follows:
>
> - for an `img` element, any resource in its list of image sources;
> - for an `input` element with a `type` attribute value of `image`, the resource referenced by its `src` attribute value;
> - for an `object` element, the resource referenced by its `data` attribute value when that resource has an image MIME type;
> - for an `image` element inside an `svg` element, the resource referenced by its `href` attribute value;
> - for an element with a computed `background-image`, each resource referenced by a url reference in that value.

The `img` bullet is the current sentence, restricted to `img`, so that case does not get narrower or wider. No example in `_rules/image-no-text-0va7u6.md` is added or removed. A search of `develop` found this definition used by that rule and by the glossary page itself.

This changes the written applicability, so a pull request should state a final-call period. I have not opened one.

LLM use: an LLM drafted this comment and the replacement sentence from the glossary, the rule, and the HTML image-source definition. The person who posts it is responsible for the text.
```
