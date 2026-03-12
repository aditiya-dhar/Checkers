# This code was generated using https://app.quicktype.io/

from enum import Enum
from typing import Any, List, Optional, Union, Dict, TypeVar, Callable, Type, cast
from uuid import UUID


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


class FlairTextColor(Enum):
    DARK = "dark"


class FlairType(Enum):
    TEXT = "text"


class Gildings:
    pass

    def __init__(self, ) -> None:
        pass

    @staticmethod
    def from_dict(obj: Any) -> 'Gildings':
        assert isinstance(obj, dict)
        return Gildings()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


class SubredditType(Enum):
    PUBLIC = "public"


class CrosspostParentList:
    approved_at_utc: None
    subreddit: str
    selftext: str
    author_fullname: str
    saved: bool
    mod_reason_title: None
    gilded: int
    clicked: bool
    title: str
    link_flair_richtext: List[Any]
    subreddit_name_prefixed: str
    hidden: bool
    pwls: int
    link_flair_css_class: str
    downs: int
    thumbnail_height: None
    top_awarded_type: None
    hide_score: bool
    name: str
    quarantine: bool
    link_flair_text_color: FlairTextColor
    upvote_ratio: float
    author_flair_background_color: None
    subreddit_type: SubredditType
    ups: int
    total_awards_received: int
    media_embed: Gildings
    thumbnail_width: None
    author_flair_template_id: None
    is_original_content: bool
    user_reports: List[Any]
    secure_media: None
    is_reddit_media_domain: bool
    is_meta: bool
    category: None
    secure_media_embed: Gildings
    link_flair_text: str
    can_mod_post: bool
    score: int
    approved_by: None
    is_created_from_ads_ui: bool
    author_premium: bool
    thumbnail: str
    edited: bool
    author_flair_css_class: None
    author_flair_richtext: List[Any]
    gildings: Gildings
    content_categories: None
    is_self: bool
    mod_note: None
    created: int
    link_flair_type: FlairType
    wls: int
    removed_by_category: None
    banned_by: None
    author_flair_type: FlairType
    domain: str
    allow_live_comments: bool
    selftext_html: str
    likes: None
    suggested_sort: None
    banned_at_utc: None
    view_count: None
    archived: bool
    no_follow: bool
    is_crosspostable: bool
    pinned: bool
    over_18: bool
    all_awardings: List[Any]
    awarders: List[Any]
    media_only: bool
    link_flair_template_id: UUID
    can_gild: bool
    spoiler: bool
    locked: bool
    author_flair_text: None
    treatment_tags: List[Any]
    visited: bool
    removed_by: None
    num_reports: None
    distinguished: None
    subreddit_id: str
    author_is_blocked: bool
    mod_reason_by: None
    removal_reason: None
    link_flair_background_color: str
    id: str
    is_robot_indexable: bool
    report_reasons: None
    author: str
    discussion_type: None
    num_comments: int
    send_replies: bool
    contest_mode: bool
    mod_reports: List[Any]
    author_patreon_flair: bool
    author_flair_text_color: None
    permalink: str
    stickied: bool
    url: str
    subreddit_subscribers: int
    created_utc: int
    num_crossposts: int
    media: None
    is_video: bool

    def __init__(self, approved_at_utc: None, subreddit: str, selftext: str, author_fullname: str, saved: bool, mod_reason_title: None, gilded: int, clicked: bool, title: str, link_flair_richtext: List[Any], subreddit_name_prefixed: str, hidden: bool, pwls: int, link_flair_css_class: str, downs: int, thumbnail_height: None, top_awarded_type: None, hide_score: bool, name: str, quarantine: bool, link_flair_text_color: FlairTextColor, upvote_ratio: float, author_flair_background_color: None, subreddit_type: SubredditType, ups: int, total_awards_received: int, media_embed: Gildings, thumbnail_width: None, author_flair_template_id: None, is_original_content: bool, user_reports: List[Any], secure_media: None, is_reddit_media_domain: bool, is_meta: bool, category: None, secure_media_embed: Gildings, link_flair_text: str, can_mod_post: bool, score: int, approved_by: None, is_created_from_ads_ui: bool, author_premium: bool, thumbnail: str, edited: bool, author_flair_css_class: None, author_flair_richtext: List[Any], gildings: Gildings, content_categories: None, is_self: bool, mod_note: None, created: int, link_flair_type: FlairType, wls: int, removed_by_category: None, banned_by: None, author_flair_type: FlairType, domain: str, allow_live_comments: bool, selftext_html: str, likes: None, suggested_sort: None, banned_at_utc: None, view_count: None, archived: bool, no_follow: bool, is_crosspostable: bool, pinned: bool, over_18: bool, all_awardings: List[Any], awarders: List[Any], media_only: bool, link_flair_template_id: UUID, can_gild: bool, spoiler: bool, locked: bool, author_flair_text: None, treatment_tags: List[Any], visited: bool, removed_by: None, num_reports: None, distinguished: None, subreddit_id: str, author_is_blocked: bool, mod_reason_by: None, removal_reason: None, link_flair_background_color: str, id: str, is_robot_indexable: bool, report_reasons: None, author: str, discussion_type: None, num_comments: int, send_replies: bool, contest_mode: bool, mod_reports: List[Any], author_patreon_flair: bool, author_flair_text_color: None, permalink: str, stickied: bool, url: str, subreddit_subscribers: int, created_utc: int, num_crossposts: int, media: None, is_video: bool) -> None:
        self.approved_at_utc = approved_at_utc
        self.subreddit = subreddit
        self.selftext = selftext
        self.author_fullname = author_fullname
        self.saved = saved
        self.mod_reason_title = mod_reason_title
        self.gilded = gilded
        self.clicked = clicked
        self.title = title
        self.link_flair_richtext = link_flair_richtext
        self.subreddit_name_prefixed = subreddit_name_prefixed
        self.hidden = hidden
        self.pwls = pwls
        self.link_flair_css_class = link_flair_css_class
        self.downs = downs
        self.thumbnail_height = thumbnail_height
        self.top_awarded_type = top_awarded_type
        self.hide_score = hide_score
        self.name = name
        self.quarantine = quarantine
        self.link_flair_text_color = link_flair_text_color
        self.upvote_ratio = upvote_ratio
        self.author_flair_background_color = author_flair_background_color
        self.subreddit_type = subreddit_type
        self.ups = ups
        self.total_awards_received = total_awards_received
        self.media_embed = media_embed
        self.thumbnail_width = thumbnail_width
        self.author_flair_template_id = author_flair_template_id
        self.is_original_content = is_original_content
        self.user_reports = user_reports
        self.secure_media = secure_media
        self.is_reddit_media_domain = is_reddit_media_domain
        self.is_meta = is_meta
        self.category = category
        self.secure_media_embed = secure_media_embed
        self.link_flair_text = link_flair_text
        self.can_mod_post = can_mod_post
        self.score = score
        self.approved_by = approved_by
        self.is_created_from_ads_ui = is_created_from_ads_ui
        self.author_premium = author_premium
        self.thumbnail = thumbnail
        self.edited = edited
        self.author_flair_css_class = author_flair_css_class
        self.author_flair_richtext = author_flair_richtext
        self.gildings = gildings
        self.content_categories = content_categories
        self.is_self = is_self
        self.mod_note = mod_note
        self.created = created
        self.link_flair_type = link_flair_type
        self.wls = wls
        self.removed_by_category = removed_by_category
        self.banned_by = banned_by
        self.author_flair_type = author_flair_type
        self.domain = domain
        self.allow_live_comments = allow_live_comments
        self.selftext_html = selftext_html
        self.likes = likes
        self.suggested_sort = suggested_sort
        self.banned_at_utc = banned_at_utc
        self.view_count = view_count
        self.archived = archived
        self.no_follow = no_follow
        self.is_crosspostable = is_crosspostable
        self.pinned = pinned
        self.over_18 = over_18
        self.all_awardings = all_awardings
        self.awarders = awarders
        self.media_only = media_only
        self.link_flair_template_id = link_flair_template_id
        self.can_gild = can_gild
        self.spoiler = spoiler
        self.locked = locked
        self.author_flair_text = author_flair_text
        self.treatment_tags = treatment_tags
        self.visited = visited
        self.removed_by = removed_by
        self.num_reports = num_reports
        self.distinguished = distinguished
        self.subreddit_id = subreddit_id
        self.author_is_blocked = author_is_blocked
        self.mod_reason_by = mod_reason_by
        self.removal_reason = removal_reason
        self.link_flair_background_color = link_flair_background_color
        self.id = id
        self.is_robot_indexable = is_robot_indexable
        self.report_reasons = report_reasons
        self.author = author
        self.discussion_type = discussion_type
        self.num_comments = num_comments
        self.send_replies = send_replies
        self.contest_mode = contest_mode
        self.mod_reports = mod_reports
        self.author_patreon_flair = author_patreon_flair
        self.author_flair_text_color = author_flair_text_color
        self.permalink = permalink
        self.stickied = stickied
        self.url = url
        self.subreddit_subscribers = subreddit_subscribers
        self.created_utc = created_utc
        self.num_crossposts = num_crossposts
        self.media = media
        self.is_video = is_video

    @staticmethod
    def from_dict(obj: Any) -> 'CrosspostParentList':
        assert isinstance(obj, dict)
        approved_at_utc = from_none(obj.get("approved_at_utc"))
        subreddit = from_str(obj.get("subreddit"))
        selftext = from_str(obj.get("selftext"))
        author_fullname = from_str(obj.get("author_fullname"))
        saved = from_bool(obj.get("saved"))
        mod_reason_title = from_none(obj.get("mod_reason_title"))
        gilded = from_int(obj.get("gilded"))
        clicked = from_bool(obj.get("clicked"))
        title = from_str(obj.get("title"))
        link_flair_richtext = from_list(lambda x: x, obj.get("link_flair_richtext"))
        subreddit_name_prefixed = from_str(obj.get("subreddit_name_prefixed"))
        hidden = from_bool(obj.get("hidden"))
        pwls = from_int(obj.get("pwls"))
        link_flair_css_class = from_str(obj.get("link_flair_css_class"))
        downs = from_int(obj.get("downs"))
        thumbnail_height = from_none(obj.get("thumbnail_height"))
        top_awarded_type = from_none(obj.get("top_awarded_type"))
        hide_score = from_bool(obj.get("hide_score"))
        name = from_str(obj.get("name"))
        quarantine = from_bool(obj.get("quarantine"))
        link_flair_text_color = FlairTextColor(obj.get("link_flair_text_color"))
        upvote_ratio = from_float(obj.get("upvote_ratio"))
        author_flair_background_color = from_none(obj.get("author_flair_background_color"))
        subreddit_type = SubredditType(obj.get("subreddit_type"))
        ups = from_int(obj.get("ups"))
        total_awards_received = from_int(obj.get("total_awards_received"))
        media_embed = Gildings.from_dict(obj.get("media_embed"))
        thumbnail_width = from_none(obj.get("thumbnail_width"))
        author_flair_template_id = from_none(obj.get("author_flair_template_id"))
        is_original_content = from_bool(obj.get("is_original_content"))
        user_reports = from_list(lambda x: x, obj.get("user_reports"))
        secure_media = from_none(obj.get("secure_media"))
        is_reddit_media_domain = from_bool(obj.get("is_reddit_media_domain"))
        is_meta = from_bool(obj.get("is_meta"))
        category = from_none(obj.get("category"))
        secure_media_embed = Gildings.from_dict(obj.get("secure_media_embed"))
        link_flair_text = from_str(obj.get("link_flair_text"))
        can_mod_post = from_bool(obj.get("can_mod_post"))
        score = from_int(obj.get("score"))
        approved_by = from_none(obj.get("approved_by"))
        is_created_from_ads_ui = from_bool(obj.get("is_created_from_ads_ui"))
        author_premium = from_bool(obj.get("author_premium"))
        thumbnail = from_str(obj.get("thumbnail"))
        edited = from_bool(obj.get("edited"))
        author_flair_css_class = from_none(obj.get("author_flair_css_class"))
        author_flair_richtext = from_list(lambda x: x, obj.get("author_flair_richtext"))
        gildings = Gildings.from_dict(obj.get("gildings"))
        content_categories = from_none(obj.get("content_categories"))
        is_self = from_bool(obj.get("is_self"))
        mod_note = from_none(obj.get("mod_note"))
        created = from_int(obj.get("created"))
        link_flair_type = FlairType(obj.get("link_flair_type"))
        wls = from_int(obj.get("wls"))
        removed_by_category = from_none(obj.get("removed_by_category"))
        banned_by = from_none(obj.get("banned_by"))
        author_flair_type = FlairType(obj.get("author_flair_type"))
        domain = from_str(obj.get("domain"))
        allow_live_comments = from_bool(obj.get("allow_live_comments"))
        selftext_html = from_str(obj.get("selftext_html"))
        likes = from_none(obj.get("likes"))
        suggested_sort = from_none(obj.get("suggested_sort"))
        banned_at_utc = from_none(obj.get("banned_at_utc"))
        view_count = from_none(obj.get("view_count"))
        archived = from_bool(obj.get("archived"))
        no_follow = from_bool(obj.get("no_follow"))
        is_crosspostable = from_bool(obj.get("is_crosspostable"))
        pinned = from_bool(obj.get("pinned"))
        over_18 = from_bool(obj.get("over_18"))
        all_awardings = from_list(lambda x: x, obj.get("all_awardings"))
        awarders = from_list(lambda x: x, obj.get("awarders"))
        media_only = from_bool(obj.get("media_only"))
        link_flair_template_id = UUID(obj.get("link_flair_template_id"))
        can_gild = from_bool(obj.get("can_gild"))
        spoiler = from_bool(obj.get("spoiler"))
        locked = from_bool(obj.get("locked"))
        author_flair_text = from_none(obj.get("author_flair_text"))
        treatment_tags = from_list(lambda x: x, obj.get("treatment_tags"))
        visited = from_bool(obj.get("visited"))
        removed_by = from_none(obj.get("removed_by"))
        num_reports = from_none(obj.get("num_reports"))
        distinguished = from_none(obj.get("distinguished"))
        subreddit_id = from_str(obj.get("subreddit_id"))
        author_is_blocked = from_bool(obj.get("author_is_blocked"))
        mod_reason_by = from_none(obj.get("mod_reason_by"))
        removal_reason = from_none(obj.get("removal_reason"))
        link_flair_background_color = from_str(obj.get("link_flair_background_color"))
        id = from_str(obj.get("id"))
        is_robot_indexable = from_bool(obj.get("is_robot_indexable"))
        report_reasons = from_none(obj.get("report_reasons"))
        author = from_str(obj.get("author"))
        discussion_type = from_none(obj.get("discussion_type"))
        num_comments = from_int(obj.get("num_comments"))
        send_replies = from_bool(obj.get("send_replies"))
        contest_mode = from_bool(obj.get("contest_mode"))
        mod_reports = from_list(lambda x: x, obj.get("mod_reports"))
        author_patreon_flair = from_bool(obj.get("author_patreon_flair"))
        author_flair_text_color = from_none(obj.get("author_flair_text_color"))
        permalink = from_str(obj.get("permalink"))
        stickied = from_bool(obj.get("stickied"))
        url = from_str(obj.get("url"))
        subreddit_subscribers = from_int(obj.get("subreddit_subscribers"))
        created_utc = from_int(obj.get("created_utc"))
        num_crossposts = from_int(obj.get("num_crossposts"))
        media = from_none(obj.get("media"))
        is_video = from_bool(obj.get("is_video"))
        return CrosspostParentList(approved_at_utc, subreddit, selftext, author_fullname, saved, mod_reason_title, gilded, clicked, title, link_flair_richtext, subreddit_name_prefixed, hidden, pwls, link_flair_css_class, downs, thumbnail_height, top_awarded_type, hide_score, name, quarantine, link_flair_text_color, upvote_ratio, author_flair_background_color, subreddit_type, ups, total_awards_received, media_embed, thumbnail_width, author_flair_template_id, is_original_content, user_reports, secure_media, is_reddit_media_domain, is_meta, category, secure_media_embed, link_flair_text, can_mod_post, score, approved_by, is_created_from_ads_ui, author_premium, thumbnail, edited, author_flair_css_class, author_flair_richtext, gildings, content_categories, is_self, mod_note, created, link_flair_type, wls, removed_by_category, banned_by, author_flair_type, domain, allow_live_comments, selftext_html, likes, suggested_sort, banned_at_utc, view_count, archived, no_follow, is_crosspostable, pinned, over_18, all_awardings, awarders, media_only, link_flair_template_id, can_gild, spoiler, locked, author_flair_text, treatment_tags, visited, removed_by, num_reports, distinguished, subreddit_id, author_is_blocked, mod_reason_by, removal_reason, link_flair_background_color, id, is_robot_indexable, report_reasons, author, discussion_type, num_comments, send_replies, contest_mode, mod_reports, author_patreon_flair, author_flair_text_color, permalink, stickied, url, subreddit_subscribers, created_utc, num_crossposts, media, is_video)

    def to_dict(self) -> dict:
        result: dict = {}
        result["approved_at_utc"] = from_none(self.approved_at_utc)
        result["subreddit"] = from_str(self.subreddit)
        result["selftext"] = from_str(self.selftext)
        result["author_fullname"] = from_str(self.author_fullname)
        result["saved"] = from_bool(self.saved)
        result["mod_reason_title"] = from_none(self.mod_reason_title)
        result["gilded"] = from_int(self.gilded)
        result["clicked"] = from_bool(self.clicked)
        result["title"] = from_str(self.title)
        result["link_flair_richtext"] = from_list(lambda x: x, self.link_flair_richtext)
        result["subreddit_name_prefixed"] = from_str(self.subreddit_name_prefixed)
        result["hidden"] = from_bool(self.hidden)
        result["pwls"] = from_int(self.pwls)
        result["link_flair_css_class"] = from_str(self.link_flair_css_class)
        result["downs"] = from_int(self.downs)
        result["thumbnail_height"] = from_none(self.thumbnail_height)
        result["top_awarded_type"] = from_none(self.top_awarded_type)
        result["hide_score"] = from_bool(self.hide_score)
        result["name"] = from_str(self.name)
        result["quarantine"] = from_bool(self.quarantine)
        result["link_flair_text_color"] = to_enum(FlairTextColor, self.link_flair_text_color)
        result["upvote_ratio"] = to_float(self.upvote_ratio)
        result["author_flair_background_color"] = from_none(self.author_flair_background_color)
        result["subreddit_type"] = to_enum(SubredditType, self.subreddit_type)
        result["ups"] = from_int(self.ups)
        result["total_awards_received"] = from_int(self.total_awards_received)
        result["media_embed"] = to_class(Gildings, self.media_embed)
        result["thumbnail_width"] = from_none(self.thumbnail_width)
        result["author_flair_template_id"] = from_none(self.author_flair_template_id)
        result["is_original_content"] = from_bool(self.is_original_content)
        result["user_reports"] = from_list(lambda x: x, self.user_reports)
        result["secure_media"] = from_none(self.secure_media)
        result["is_reddit_media_domain"] = from_bool(self.is_reddit_media_domain)
        result["is_meta"] = from_bool(self.is_meta)
        result["category"] = from_none(self.category)
        result["secure_media_embed"] = to_class(Gildings, self.secure_media_embed)
        result["link_flair_text"] = from_str(self.link_flair_text)
        result["can_mod_post"] = from_bool(self.can_mod_post)
        result["score"] = from_int(self.score)
        result["approved_by"] = from_none(self.approved_by)
        result["is_created_from_ads_ui"] = from_bool(self.is_created_from_ads_ui)
        result["author_premium"] = from_bool(self.author_premium)
        result["thumbnail"] = from_str(self.thumbnail)
        result["edited"] = from_bool(self.edited)
        result["author_flair_css_class"] = from_none(self.author_flair_css_class)
        result["author_flair_richtext"] = from_list(lambda x: x, self.author_flair_richtext)
        result["gildings"] = to_class(Gildings, self.gildings)
        result["content_categories"] = from_none(self.content_categories)
        result["is_self"] = from_bool(self.is_self)
        result["mod_note"] = from_none(self.mod_note)
        result["created"] = from_int(self.created)
        result["link_flair_type"] = to_enum(FlairType, self.link_flair_type)
        result["wls"] = from_int(self.wls)
        result["removed_by_category"] = from_none(self.removed_by_category)
        result["banned_by"] = from_none(self.banned_by)
        result["author_flair_type"] = to_enum(FlairType, self.author_flair_type)
        result["domain"] = from_str(self.domain)
        result["allow_live_comments"] = from_bool(self.allow_live_comments)
        result["selftext_html"] = from_str(self.selftext_html)
        result["likes"] = from_none(self.likes)
        result["suggested_sort"] = from_none(self.suggested_sort)
        result["banned_at_utc"] = from_none(self.banned_at_utc)
        result["view_count"] = from_none(self.view_count)
        result["archived"] = from_bool(self.archived)
        result["no_follow"] = from_bool(self.no_follow)
        result["is_crosspostable"] = from_bool(self.is_crosspostable)
        result["pinned"] = from_bool(self.pinned)
        result["over_18"] = from_bool(self.over_18)
        result["all_awardings"] = from_list(lambda x: x, self.all_awardings)
        result["awarders"] = from_list(lambda x: x, self.awarders)
        result["media_only"] = from_bool(self.media_only)
        result["link_flair_template_id"] = str(self.link_flair_template_id)
        result["can_gild"] = from_bool(self.can_gild)
        result["spoiler"] = from_bool(self.spoiler)
        result["locked"] = from_bool(self.locked)
        result["author_flair_text"] = from_none(self.author_flair_text)
        result["treatment_tags"] = from_list(lambda x: x, self.treatment_tags)
        result["visited"] = from_bool(self.visited)
        result["removed_by"] = from_none(self.removed_by)
        result["num_reports"] = from_none(self.num_reports)
        result["distinguished"] = from_none(self.distinguished)
        result["subreddit_id"] = from_str(self.subreddit_id)
        result["author_is_blocked"] = from_bool(self.author_is_blocked)
        result["mod_reason_by"] = from_none(self.mod_reason_by)
        result["removal_reason"] = from_none(self.removal_reason)
        result["link_flair_background_color"] = from_str(self.link_flair_background_color)
        result["id"] = from_str(self.id)
        result["is_robot_indexable"] = from_bool(self.is_robot_indexable)
        result["report_reasons"] = from_none(self.report_reasons)
        result["author"] = from_str(self.author)
        result["discussion_type"] = from_none(self.discussion_type)
        result["num_comments"] = from_int(self.num_comments)
        result["send_replies"] = from_bool(self.send_replies)
        result["contest_mode"] = from_bool(self.contest_mode)
        result["mod_reports"] = from_list(lambda x: x, self.mod_reports)
        result["author_patreon_flair"] = from_bool(self.author_patreon_flair)
        result["author_flair_text_color"] = from_none(self.author_flair_text_color)
        result["permalink"] = from_str(self.permalink)
        result["stickied"] = from_bool(self.stickied)
        result["url"] = from_str(self.url)
        result["subreddit_subscribers"] = from_int(self.subreddit_subscribers)
        result["created_utc"] = from_int(self.created_utc)
        result["num_crossposts"] = from_int(self.num_crossposts)
        result["media"] = from_none(self.media)
        result["is_video"] = from_bool(self.is_video)
        return result


class Item:
    caption: str
    media_id: str
    id: int

    def __init__(self, caption: str, media_id: str, id: int) -> None:
        self.caption = caption
        self.media_id = media_id
        self.id = id

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        caption = from_str(obj.get("caption"))
        media_id = from_str(obj.get("media_id"))
        id = from_int(obj.get("id"))
        return Item(caption, media_id, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["caption"] = from_str(self.caption)
        result["media_id"] = from_str(self.media_id)
        result["id"] = from_int(self.id)
        return result


class GalleryData:
    items: List[Item]

    def __init__(self, items: List[Item]) -> None:
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'GalleryData':
        assert isinstance(obj, dict)
        items = from_list(Item.from_dict, obj.get("items"))
        return GalleryData(items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["items"] = from_list(lambda x: to_class(Item, x), self.items)
        return result


class S:
    y: int
    x: int
    u: str

    def __init__(self, y: int, x: int, u: str) -> None:
        self.y = y
        self.x = x
        self.u = u

    @staticmethod
    def from_dict(obj: Any) -> 'S':
        assert isinstance(obj, dict)
        y = from_int(obj.get("y"))
        x = from_int(obj.get("x"))
        u = from_str(obj.get("u"))
        return S(y, x, u)

    def to_dict(self) -> dict:
        result: dict = {}
        result["y"] = from_int(self.y)
        result["x"] = from_int(self.x)
        result["u"] = from_str(self.u)
        return result


class MediaMetadatum:
    status: str
    e: str
    m: str
    p: List[S]
    s: S
    id: str

    def __init__(self, status: str, e: str, m: str, p: List[S], s: S, id: str) -> None:
        self.status = status
        self.e = e
        self.m = m
        self.p = p
        self.s = s
        self.id = id

    @staticmethod
    def from_dict(obj: Any) -> 'MediaMetadatum':
        assert isinstance(obj, dict)
        status = from_str(obj.get("status"))
        e = from_str(obj.get("e"))
        m = from_str(obj.get("m"))
        p = from_list(S.from_dict, obj.get("p"))
        s = S.from_dict(obj.get("s"))
        id = from_str(obj.get("id"))
        return MediaMetadatum(status, e, m, p, s, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["status"] = from_str(self.status)
        result["e"] = from_str(self.e)
        result["m"] = from_str(self.m)
        result["p"] = from_list(lambda x: to_class(S, x), self.p)
        result["s"] = to_class(S, self.s)
        result["id"] = from_str(self.id)
        return result


class Source:
    url: str
    width: int
    height: int

    def __init__(self, url: str, width: int, height: int) -> None:
        self.url = url
        self.width = width
        self.height = height

    @staticmethod
    def from_dict(obj: Any) -> 'Source':
        assert isinstance(obj, dict)
        url = from_str(obj.get("url"))
        width = from_int(obj.get("width"))
        height = from_int(obj.get("height"))
        return Source(url, width, height)

    def to_dict(self) -> dict:
        result: dict = {}
        result["url"] = from_str(self.url)
        result["width"] = from_int(self.width)
        result["height"] = from_int(self.height)
        return result


class Image:
    source: Source
    resolutions: List[Source]
    variants: Gildings
    id: str

    def __init__(self, source: Source, resolutions: List[Source], variants: Gildings, id: str) -> None:
        self.source = source
        self.resolutions = resolutions
        self.variants = variants
        self.id = id

    @staticmethod
    def from_dict(obj: Any) -> 'Image':
        assert isinstance(obj, dict)
        source = Source.from_dict(obj.get("source"))
        resolutions = from_list(Source.from_dict, obj.get("resolutions"))
        variants = Gildings.from_dict(obj.get("variants"))
        id = from_str(obj.get("id"))
        return Image(source, resolutions, variants, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["source"] = to_class(Source, self.source)
        result["resolutions"] = from_list(lambda x: to_class(Source, x), self.resolutions)
        result["variants"] = to_class(Gildings, self.variants)
        result["id"] = from_str(self.id)
        return result


class Preview:
    images: List[Image]
    enabled: bool

    def __init__(self, images: List[Image], enabled: bool) -> None:
        self.images = images
        self.enabled = enabled

    @staticmethod
    def from_dict(obj: Any) -> 'Preview':
        assert isinstance(obj, dict)
        images = from_list(Image.from_dict, obj.get("images"))
        enabled = from_bool(obj.get("enabled"))
        return Preview(images, enabled)

    def to_dict(self) -> dict:
        result: dict = {}
        result["images"] = from_list(lambda x: to_class(Image, x), self.images)
        result["enabled"] = from_bool(self.enabled)
        return result


class Subreddit(Enum):
    TEMPLE = "Temple"


class SubredditID(Enum):
    T5_2_RO0_V = "t5_2ro0v"


class SubredditNamePrefixed(Enum):
    R_TEMPLE = "r/Temple"


class ChildData:
    approved_at_utc: None
    subreddit: Subreddit
    selftext: str
    author_fullname: str
    saved: bool
    mod_reason_title: None
    gilded: int
    clicked: bool
    title: str
    link_flair_richtext: List[Any]
    subreddit_name_prefixed: SubredditNamePrefixed
    hidden: bool
    pwls: int
    link_flair_css_class: Optional[str]
    downs: int
    thumbnail_height: Optional[int]
    top_awarded_type: None
    hide_score: bool
    name: str
    quarantine: bool
    link_flair_text_color: FlairTextColor
    upvote_ratio: float
    author_flair_background_color: None
    subreddit_type: SubredditType
    ups: int
    total_awards_received: int
    media_embed: Gildings
    thumbnail_width: Optional[int]
    author_flair_template_id: Optional[UUID]
    is_original_content: bool
    user_reports: List[Any]
    secure_media: None
    is_reddit_media_domain: bool
    is_meta: bool
    category: None
    secure_media_embed: Gildings
    link_flair_text: Optional[str]
    can_mod_post: bool
    score: int
    approved_by: None
    is_created_from_ads_ui: bool
    author_premium: bool
    thumbnail: str
    edited: Union[bool, int]
    author_flair_css_class: None
    author_flair_richtext: List[Any]
    gildings: Gildings
    content_categories: None
    is_self: bool
    mod_note: None
    created: int
    link_flair_type: FlairType
    wls: int
    removed_by_category: None
    banned_by: None
    author_flair_type: FlairType
    domain: str
    allow_live_comments: bool
    selftext_html: Optional[str]
    likes: None
    suggested_sort: None
    banned_at_utc: None
    view_count: None
    archived: bool
    no_follow: bool
    is_crosspostable: bool
    pinned: bool
    over_18: bool
    all_awardings: List[Any]
    awarders: List[Any]
    media_only: bool
    link_flair_template_id: Optional[UUID]
    can_gild: bool
    spoiler: bool
    locked: bool
    author_flair_text: Optional[str]
    treatment_tags: List[Any]
    visited: bool
    removed_by: None
    num_reports: None
    distinguished: Optional[str]
    subreddit_id: SubredditID
    author_is_blocked: bool
    mod_reason_by: None
    removal_reason: None
    link_flair_background_color: str
    id: str
    is_robot_indexable: bool
    report_reasons: None
    author: str
    discussion_type: None
    num_comments: int
    send_replies: bool
    contest_mode: bool
    mod_reports: List[Any]
    author_patreon_flair: bool
    author_flair_text_color: Optional[FlairTextColor]
    permalink: str
    stickied: bool
    url: str
    subreddit_subscribers: int
    created_utc: int
    num_crossposts: int
    media: None
    is_video: bool
    post_hint: Optional[str]
    url_overridden_by_dest: Optional[str]
    preview: Optional[Preview]
    crosspost_parent_list: Optional[List[CrosspostParentList]]
    crosspost_parent: Optional[str]
    is_gallery: Optional[bool]
    media_metadata: Optional[Dict[str, MediaMetadatum]]
    gallery_data: Optional[GalleryData]

    def __init__(self, approved_at_utc: None, subreddit: Subreddit, selftext: str, author_fullname: str, saved: bool, mod_reason_title: None, gilded: int, clicked: bool, title: str, link_flair_richtext: List[Any], subreddit_name_prefixed: SubredditNamePrefixed, hidden: bool, pwls: int, link_flair_css_class: Optional[str], downs: int, thumbnail_height: Optional[int], top_awarded_type: None, hide_score: bool, name: str, quarantine: bool, link_flair_text_color: FlairTextColor, upvote_ratio: float, author_flair_background_color: None, subreddit_type: SubredditType, ups: int, total_awards_received: int, media_embed: Gildings, thumbnail_width: Optional[int], author_flair_template_id: Optional[UUID], is_original_content: bool, user_reports: List[Any], secure_media: None, is_reddit_media_domain: bool, is_meta: bool, category: None, secure_media_embed: Gildings, link_flair_text: Optional[str], can_mod_post: bool, score: int, approved_by: None, is_created_from_ads_ui: bool, author_premium: bool, thumbnail: str, edited: Union[bool, int], author_flair_css_class: None, author_flair_richtext: List[Any], gildings: Gildings, content_categories: None, is_self: bool, mod_note: None, created: int, link_flair_type: FlairType, wls: int, removed_by_category: None, banned_by: None, author_flair_type: FlairType, domain: str, allow_live_comments: bool, selftext_html: Optional[str], likes: None, suggested_sort: None, banned_at_utc: None, view_count: None, archived: bool, no_follow: bool, is_crosspostable: bool, pinned: bool, over_18: bool, all_awardings: List[Any], awarders: List[Any], media_only: bool, link_flair_template_id: Optional[UUID], can_gild: bool, spoiler: bool, locked: bool, author_flair_text: Optional[str], treatment_tags: List[Any], visited: bool, removed_by: None, num_reports: None, distinguished: Optional[str], subreddit_id: SubredditID, author_is_blocked: bool, mod_reason_by: None, removal_reason: None, link_flair_background_color: str, id: str, is_robot_indexable: bool, report_reasons: None, author: str, discussion_type: None, num_comments: int, send_replies: bool, contest_mode: bool, mod_reports: List[Any], author_patreon_flair: bool, author_flair_text_color: Optional[FlairTextColor], permalink: str, stickied: bool, url: str, subreddit_subscribers: int, created_utc: int, num_crossposts: int, media: None, is_video: bool, post_hint: Optional[str], url_overridden_by_dest: Optional[str], preview: Optional[Preview], crosspost_parent_list: Optional[List[CrosspostParentList]], crosspost_parent: Optional[str], is_gallery: Optional[bool], media_metadata: Optional[Dict[str, MediaMetadatum]], gallery_data: Optional[GalleryData]) -> None:
        self.approved_at_utc = approved_at_utc
        self.subreddit = subreddit
        self.selftext = selftext
        self.author_fullname = author_fullname
        self.saved = saved
        self.mod_reason_title = mod_reason_title
        self.gilded = gilded
        self.clicked = clicked
        self.title = title
        self.link_flair_richtext = link_flair_richtext
        self.subreddit_name_prefixed = subreddit_name_prefixed
        self.hidden = hidden
        self.pwls = pwls
        self.link_flair_css_class = link_flair_css_class
        self.downs = downs
        self.thumbnail_height = thumbnail_height
        self.top_awarded_type = top_awarded_type
        self.hide_score = hide_score
        self.name = name
        self.quarantine = quarantine
        self.link_flair_text_color = link_flair_text_color
        self.upvote_ratio = upvote_ratio
        self.author_flair_background_color = author_flair_background_color
        self.subreddit_type = subreddit_type
        self.ups = ups
        self.total_awards_received = total_awards_received
        self.media_embed = media_embed
        self.thumbnail_width = thumbnail_width
        self.author_flair_template_id = author_flair_template_id
        self.is_original_content = is_original_content
        self.user_reports = user_reports
        self.secure_media = secure_media
        self.is_reddit_media_domain = is_reddit_media_domain
        self.is_meta = is_meta
        self.category = category
        self.secure_media_embed = secure_media_embed
        self.link_flair_text = link_flair_text
        self.can_mod_post = can_mod_post
        self.score = score
        self.approved_by = approved_by
        self.is_created_from_ads_ui = is_created_from_ads_ui
        self.author_premium = author_premium
        self.thumbnail = thumbnail
        self.edited = edited
        self.author_flair_css_class = author_flair_css_class
        self.author_flair_richtext = author_flair_richtext
        self.gildings = gildings
        self.content_categories = content_categories
        self.is_self = is_self
        self.mod_note = mod_note
        self.created = created
        self.link_flair_type = link_flair_type
        self.wls = wls
        self.removed_by_category = removed_by_category
        self.banned_by = banned_by
        self.author_flair_type = author_flair_type
        self.domain = domain
        self.allow_live_comments = allow_live_comments
        self.selftext_html = selftext_html
        self.likes = likes
        self.suggested_sort = suggested_sort
        self.banned_at_utc = banned_at_utc
        self.view_count = view_count
        self.archived = archived
        self.no_follow = no_follow
        self.is_crosspostable = is_crosspostable
        self.pinned = pinned
        self.over_18 = over_18
        self.all_awardings = all_awardings
        self.awarders = awarders
        self.media_only = media_only
        self.link_flair_template_id = link_flair_template_id
        self.can_gild = can_gild
        self.spoiler = spoiler
        self.locked = locked
        self.author_flair_text = author_flair_text
        self.treatment_tags = treatment_tags
        self.visited = visited
        self.removed_by = removed_by
        self.num_reports = num_reports
        self.distinguished = distinguished
        self.subreddit_id = subreddit_id
        self.author_is_blocked = author_is_blocked
        self.mod_reason_by = mod_reason_by
        self.removal_reason = removal_reason
        self.link_flair_background_color = link_flair_background_color
        self.id = id
        self.is_robot_indexable = is_robot_indexable
        self.report_reasons = report_reasons
        self.author = author
        self.discussion_type = discussion_type
        self.num_comments = num_comments
        self.send_replies = send_replies
        self.contest_mode = contest_mode
        self.mod_reports = mod_reports
        self.author_patreon_flair = author_patreon_flair
        self.author_flair_text_color = author_flair_text_color
        self.permalink = permalink
        self.stickied = stickied
        self.url = url
        self.subreddit_subscribers = subreddit_subscribers
        self.created_utc = created_utc
        self.num_crossposts = num_crossposts
        self.media = media
        self.is_video = is_video
        self.post_hint = post_hint
        self.url_overridden_by_dest = url_overridden_by_dest
        self.preview = preview
        self.crosspost_parent_list = crosspost_parent_list
        self.crosspost_parent = crosspost_parent
        self.is_gallery = is_gallery
        self.media_metadata = media_metadata
        self.gallery_data = gallery_data

    @staticmethod
    def from_dict(obj: Any) -> 'ChildData':
        assert isinstance(obj, dict)
        approved_at_utc = from_none(obj.get("approved_at_utc"))
        subreddit = Subreddit(obj.get("subreddit"))
        selftext = from_str(obj.get("selftext"))
        author_fullname = from_str(obj.get("author_fullname"))
        saved = from_bool(obj.get("saved"))
        mod_reason_title = from_none(obj.get("mod_reason_title"))
        gilded = from_int(obj.get("gilded"))
        clicked = from_bool(obj.get("clicked"))
        title = from_str(obj.get("title"))
        link_flair_richtext = from_list(lambda x: x, obj.get("link_flair_richtext"))
        subreddit_name_prefixed = SubredditNamePrefixed(obj.get("subreddit_name_prefixed"))
        hidden = from_bool(obj.get("hidden"))
        pwls = from_int(obj.get("pwls"))
        link_flair_css_class = from_union([from_none, from_str], obj.get("link_flair_css_class"))
        downs = from_int(obj.get("downs"))
        thumbnail_height = from_union([from_none, from_int], obj.get("thumbnail_height"))
        top_awarded_type = from_none(obj.get("top_awarded_type"))
        hide_score = from_bool(obj.get("hide_score"))
        name = from_str(obj.get("name"))
        quarantine = from_bool(obj.get("quarantine"))
        link_flair_text_color = FlairTextColor(obj.get("link_flair_text_color"))
        upvote_ratio = from_float(obj.get("upvote_ratio"))
        author_flair_background_color = from_none(obj.get("author_flair_background_color"))
        subreddit_type = SubredditType(obj.get("subreddit_type"))
        ups = from_int(obj.get("ups"))
        total_awards_received = from_int(obj.get("total_awards_received"))
        media_embed = Gildings.from_dict(obj.get("media_embed"))
        thumbnail_width = from_union([from_none, from_int], obj.get("thumbnail_width"))
        author_flair_template_id = from_union([from_none, lambda x: UUID(x)], obj.get("author_flair_template_id"))
        is_original_content = from_bool(obj.get("is_original_content"))
        user_reports = from_list(lambda x: x, obj.get("user_reports"))
        secure_media = from_none(obj.get("secure_media"))
        is_reddit_media_domain = from_bool(obj.get("is_reddit_media_domain"))
        is_meta = from_bool(obj.get("is_meta"))
        category = from_none(obj.get("category"))
        secure_media_embed = Gildings.from_dict(obj.get("secure_media_embed"))
        link_flair_text = from_union([from_none, from_str], obj.get("link_flair_text"))
        can_mod_post = from_bool(obj.get("can_mod_post"))
        score = from_int(obj.get("score"))
        approved_by = from_none(obj.get("approved_by"))
        is_created_from_ads_ui = from_bool(obj.get("is_created_from_ads_ui"))
        author_premium = from_bool(obj.get("author_premium"))
        thumbnail = from_str(obj.get("thumbnail"))
        edited = from_union([from_bool, from_int], obj.get("edited"))
        author_flair_css_class = from_none(obj.get("author_flair_css_class"))
        author_flair_richtext = from_list(lambda x: x, obj.get("author_flair_richtext"))
        gildings = Gildings.from_dict(obj.get("gildings"))
        content_categories = from_none(obj.get("content_categories"))
        is_self = from_bool(obj.get("is_self"))
        mod_note = from_none(obj.get("mod_note"))
        created = from_int(obj.get("created"))
        link_flair_type = FlairType(obj.get("link_flair_type"))
        wls = from_int(obj.get("wls"))
        removed_by_category = from_none(obj.get("removed_by_category"))
        banned_by = from_none(obj.get("banned_by"))
        author_flair_type = FlairType(obj.get("author_flair_type"))
        domain = from_str(obj.get("domain"))
        allow_live_comments = from_bool(obj.get("allow_live_comments"))
        selftext_html = from_union([from_none, from_str], obj.get("selftext_html"))
        likes = from_none(obj.get("likes"))
        suggested_sort = from_none(obj.get("suggested_sort"))
        banned_at_utc = from_none(obj.get("banned_at_utc"))
        view_count = from_none(obj.get("view_count"))
        archived = from_bool(obj.get("archived"))
        no_follow = from_bool(obj.get("no_follow"))
        is_crosspostable = from_bool(obj.get("is_crosspostable"))
        pinned = from_bool(obj.get("pinned"))
        over_18 = from_bool(obj.get("over_18"))
        all_awardings = from_list(lambda x: x, obj.get("all_awardings"))
        awarders = from_list(lambda x: x, obj.get("awarders"))
        media_only = from_bool(obj.get("media_only"))
        link_flair_template_id = from_union([from_none, lambda x: UUID(x)], obj.get("link_flair_template_id"))
        can_gild = from_bool(obj.get("can_gild"))
        spoiler = from_bool(obj.get("spoiler"))
        locked = from_bool(obj.get("locked"))
        author_flair_text = from_union([from_none, from_str], obj.get("author_flair_text"))
        treatment_tags = from_list(lambda x: x, obj.get("treatment_tags"))
        visited = from_bool(obj.get("visited"))
        removed_by = from_none(obj.get("removed_by"))
        num_reports = from_none(obj.get("num_reports"))
        distinguished = from_union([from_none, from_str], obj.get("distinguished"))
        subreddit_id = SubredditID(obj.get("subreddit_id"))
        author_is_blocked = from_bool(obj.get("author_is_blocked"))
        mod_reason_by = from_none(obj.get("mod_reason_by"))
        removal_reason = from_none(obj.get("removal_reason"))
        link_flair_background_color = from_str(obj.get("link_flair_background_color"))
        id = from_str(obj.get("id"))
        is_robot_indexable = from_bool(obj.get("is_robot_indexable"))
        report_reasons = from_none(obj.get("report_reasons"))
        author = from_str(obj.get("author"))
        discussion_type = from_none(obj.get("discussion_type"))
        num_comments = from_int(obj.get("num_comments"))
        send_replies = from_bool(obj.get("send_replies"))
        contest_mode = from_bool(obj.get("contest_mode"))
        mod_reports = from_list(lambda x: x, obj.get("mod_reports"))
        author_patreon_flair = from_bool(obj.get("author_patreon_flair"))
        author_flair_text_color = from_union([from_none, FlairTextColor], obj.get("author_flair_text_color"))
        permalink = from_str(obj.get("permalink"))
        stickied = from_bool(obj.get("stickied"))
        url = from_str(obj.get("url"))
        subreddit_subscribers = from_int(obj.get("subreddit_subscribers"))
        created_utc = from_int(obj.get("created_utc"))
        num_crossposts = from_int(obj.get("num_crossposts"))
        media = from_none(obj.get("media"))
        is_video = from_bool(obj.get("is_video"))
        post_hint = from_union([from_str, from_none], obj.get("post_hint"))
        url_overridden_by_dest = from_union([from_str, from_none], obj.get("url_overridden_by_dest"))
        preview = from_union([Preview.from_dict, from_none], obj.get("preview"))
        crosspost_parent_list = from_union([lambda x: from_list(CrosspostParentList.from_dict, x), from_none], obj.get("crosspost_parent_list"))
        crosspost_parent = from_union([from_str, from_none], obj.get("crosspost_parent"))
        is_gallery = from_union([from_bool, from_none], obj.get("is_gallery"))
        media_metadata = from_union([lambda x: from_dict(MediaMetadatum.from_dict, x), from_none], obj.get("media_metadata"))
        gallery_data = from_union([GalleryData.from_dict, from_none], obj.get("gallery_data"))
        return ChildData(approved_at_utc, subreddit, selftext, author_fullname, saved, mod_reason_title, gilded, clicked, title, link_flair_richtext, subreddit_name_prefixed, hidden, pwls, link_flair_css_class, downs, thumbnail_height, top_awarded_type, hide_score, name, quarantine, link_flair_text_color, upvote_ratio, author_flair_background_color, subreddit_type, ups, total_awards_received, media_embed, thumbnail_width, author_flair_template_id, is_original_content, user_reports, secure_media, is_reddit_media_domain, is_meta, category, secure_media_embed, link_flair_text, can_mod_post, score, approved_by, is_created_from_ads_ui, author_premium, thumbnail, edited, author_flair_css_class, author_flair_richtext, gildings, content_categories, is_self, mod_note, created, link_flair_type, wls, removed_by_category, banned_by, author_flair_type, domain, allow_live_comments, selftext_html, likes, suggested_sort, banned_at_utc, view_count, archived, no_follow, is_crosspostable, pinned, over_18, all_awardings, awarders, media_only, link_flair_template_id, can_gild, spoiler, locked, author_flair_text, treatment_tags, visited, removed_by, num_reports, distinguished, subreddit_id, author_is_blocked, mod_reason_by, removal_reason, link_flair_background_color, id, is_robot_indexable, report_reasons, author, discussion_type, num_comments, send_replies, contest_mode, mod_reports, author_patreon_flair, author_flair_text_color, permalink, stickied, url, subreddit_subscribers, created_utc, num_crossposts, media, is_video, post_hint, url_overridden_by_dest, preview, crosspost_parent_list, crosspost_parent, is_gallery, media_metadata, gallery_data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["approved_at_utc"] = from_none(self.approved_at_utc)
        result["subreddit"] = to_enum(Subreddit, self.subreddit)
        result["selftext"] = from_str(self.selftext)
        result["author_fullname"] = from_str(self.author_fullname)
        result["saved"] = from_bool(self.saved)
        result["mod_reason_title"] = from_none(self.mod_reason_title)
        result["gilded"] = from_int(self.gilded)
        result["clicked"] = from_bool(self.clicked)
        result["title"] = from_str(self.title)
        result["link_flair_richtext"] = from_list(lambda x: x, self.link_flair_richtext)
        result["subreddit_name_prefixed"] = to_enum(SubredditNamePrefixed, self.subreddit_name_prefixed)
        result["hidden"] = from_bool(self.hidden)
        result["pwls"] = from_int(self.pwls)
        result["link_flair_css_class"] = from_union([from_none, from_str], self.link_flair_css_class)
        result["downs"] = from_int(self.downs)
        result["thumbnail_height"] = from_union([from_none, from_int], self.thumbnail_height)
        result["top_awarded_type"] = from_none(self.top_awarded_type)
        result["hide_score"] = from_bool(self.hide_score)
        result["name"] = from_str(self.name)
        result["quarantine"] = from_bool(self.quarantine)
        result["link_flair_text_color"] = to_enum(FlairTextColor, self.link_flair_text_color)
        result["upvote_ratio"] = to_float(self.upvote_ratio)
        result["author_flair_background_color"] = from_none(self.author_flair_background_color)
        result["subreddit_type"] = to_enum(SubredditType, self.subreddit_type)
        result["ups"] = from_int(self.ups)
        result["total_awards_received"] = from_int(self.total_awards_received)
        result["media_embed"] = to_class(Gildings, self.media_embed)
        result["thumbnail_width"] = from_union([from_none, from_int], self.thumbnail_width)
        result["author_flair_template_id"] = from_union([from_none, lambda x: str(x)], self.author_flair_template_id)
        result["is_original_content"] = from_bool(self.is_original_content)
        result["user_reports"] = from_list(lambda x: x, self.user_reports)
        result["secure_media"] = from_none(self.secure_media)
        result["is_reddit_media_domain"] = from_bool(self.is_reddit_media_domain)
        result["is_meta"] = from_bool(self.is_meta)
        result["category"] = from_none(self.category)
        result["secure_media_embed"] = to_class(Gildings, self.secure_media_embed)
        result["link_flair_text"] = from_union([from_none, from_str], self.link_flair_text)
        result["can_mod_post"] = from_bool(self.can_mod_post)
        result["score"] = from_int(self.score)
        result["approved_by"] = from_none(self.approved_by)
        result["is_created_from_ads_ui"] = from_bool(self.is_created_from_ads_ui)
        result["author_premium"] = from_bool(self.author_premium)
        result["thumbnail"] = from_str(self.thumbnail)
        result["edited"] = from_union([from_bool, from_int], self.edited)
        result["author_flair_css_class"] = from_none(self.author_flair_css_class)
        result["author_flair_richtext"] = from_list(lambda x: x, self.author_flair_richtext)
        result["gildings"] = to_class(Gildings, self.gildings)
        result["content_categories"] = from_none(self.content_categories)
        result["is_self"] = from_bool(self.is_self)
        result["mod_note"] = from_none(self.mod_note)
        result["created"] = from_int(self.created)
        result["link_flair_type"] = to_enum(FlairType, self.link_flair_type)
        result["wls"] = from_int(self.wls)
        result["removed_by_category"] = from_none(self.removed_by_category)
        result["banned_by"] = from_none(self.banned_by)
        result["author_flair_type"] = to_enum(FlairType, self.author_flair_type)
        result["domain"] = from_str(self.domain)
        result["allow_live_comments"] = from_bool(self.allow_live_comments)
        result["selftext_html"] = from_union([from_none, from_str], self.selftext_html)
        result["likes"] = from_none(self.likes)
        result["suggested_sort"] = from_none(self.suggested_sort)
        result["banned_at_utc"] = from_none(self.banned_at_utc)
        result["view_count"] = from_none(self.view_count)
        result["archived"] = from_bool(self.archived)
        result["no_follow"] = from_bool(self.no_follow)
        result["is_crosspostable"] = from_bool(self.is_crosspostable)
        result["pinned"] = from_bool(self.pinned)
        result["over_18"] = from_bool(self.over_18)
        result["all_awardings"] = from_list(lambda x: x, self.all_awardings)
        result["awarders"] = from_list(lambda x: x, self.awarders)
        result["media_only"] = from_bool(self.media_only)
        if self.link_flair_template_id is not None:
            result["link_flair_template_id"] = from_union([from_none, lambda x: str(x)], self.link_flair_template_id)
        result["can_gild"] = from_bool(self.can_gild)
        result["spoiler"] = from_bool(self.spoiler)
        result["locked"] = from_bool(self.locked)
        result["author_flair_text"] = from_union([from_none, from_str], self.author_flair_text)
        result["treatment_tags"] = from_list(lambda x: x, self.treatment_tags)
        result["visited"] = from_bool(self.visited)
        result["removed_by"] = from_none(self.removed_by)
        result["num_reports"] = from_none(self.num_reports)
        result["distinguished"] = from_union([from_none, from_str], self.distinguished)
        result["subreddit_id"] = to_enum(SubredditID, self.subreddit_id)
        result["author_is_blocked"] = from_bool(self.author_is_blocked)
        result["mod_reason_by"] = from_none(self.mod_reason_by)
        result["removal_reason"] = from_none(self.removal_reason)
        result["link_flair_background_color"] = from_str(self.link_flair_background_color)
        result["id"] = from_str(self.id)
        result["is_robot_indexable"] = from_bool(self.is_robot_indexable)
        result["report_reasons"] = from_none(self.report_reasons)
        result["author"] = from_str(self.author)
        result["discussion_type"] = from_none(self.discussion_type)
        result["num_comments"] = from_int(self.num_comments)
        result["send_replies"] = from_bool(self.send_replies)
        result["contest_mode"] = from_bool(self.contest_mode)
        result["mod_reports"] = from_list(lambda x: x, self.mod_reports)
        result["author_patreon_flair"] = from_bool(self.author_patreon_flair)
        result["author_flair_text_color"] = from_union([from_none, lambda x: to_enum(FlairTextColor, x)], self.author_flair_text_color)
        result["permalink"] = from_str(self.permalink)
        result["stickied"] = from_bool(self.stickied)
        result["url"] = from_str(self.url)
        result["subreddit_subscribers"] = from_int(self.subreddit_subscribers)
        result["created_utc"] = from_int(self.created_utc)
        result["num_crossposts"] = from_int(self.num_crossposts)
        result["media"] = from_none(self.media)
        result["is_video"] = from_bool(self.is_video)
        if self.post_hint is not None:
            result["post_hint"] = from_union([from_str, from_none], self.post_hint)
        if self.url_overridden_by_dest is not None:
            result["url_overridden_by_dest"] = from_union([from_str, from_none], self.url_overridden_by_dest)
        if self.preview is not None:
            result["preview"] = from_union([lambda x: to_class(Preview, x), from_none], self.preview)
        if self.crosspost_parent_list is not None:
            result["crosspost_parent_list"] = from_union([lambda x: from_list(lambda x: to_class(CrosspostParentList, x), x), from_none], self.crosspost_parent_list)
        if self.crosspost_parent is not None:
            result["crosspost_parent"] = from_union([from_str, from_none], self.crosspost_parent)
        if self.is_gallery is not None:
            result["is_gallery"] = from_union([from_bool, from_none], self.is_gallery)
        if self.media_metadata is not None:
            result["media_metadata"] = from_union([lambda x: from_dict(lambda x: to_class(MediaMetadatum, x), x), from_none], self.media_metadata)
        if self.gallery_data is not None:
            result["gallery_data"] = from_union([lambda x: to_class(GalleryData, x), from_none], self.gallery_data)
        return result


class Kind(Enum):
    T3 = "t3"


class Child:
    kind: Kind
    data: ChildData

    def __init__(self, kind: Kind, data: ChildData) -> None:
        self.kind = kind
        self.data = data

    @staticmethod
    def from_dict(obj: Any) -> 'Child':
        assert isinstance(obj, dict)
        kind = Kind(obj.get("kind"))
        data = ChildData.from_dict(obj.get("data"))
        return Child(kind, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["kind"] = to_enum(Kind, self.kind)
        result["data"] = to_class(ChildData, self.data)
        return result


class RedditResponseData:
    after: str
    dist: int
    modhash: str
    geo_filter: None
    children: List[Child]
    before: None

    def __init__(self, after: str, dist: int, modhash: str, geo_filter: None, children: List[Child], before: None) -> None:
        self.after = after
        self.dist = dist
        self.modhash = modhash
        self.geo_filter = geo_filter
        self.children = children
        self.before = before

    @staticmethod
    def from_dict(obj: Any) -> 'RedditResponseData':
        assert isinstance(obj, dict)
        after = from_str(obj.get("after"))
        dist = from_int(obj.get("dist"))
        modhash = from_str(obj.get("modhash"))
        geo_filter = from_none(obj.get("geo_filter"))
        children = from_list(Child.from_dict, obj.get("children"))
        before = from_none(obj.get("before"))
        return RedditResponseData(after, dist, modhash, geo_filter, children, before)

    def to_dict(self) -> dict:
        result: dict = {}
        result["after"] = from_str(self.after)
        result["dist"] = from_int(self.dist)
        result["modhash"] = from_str(self.modhash)
        result["geo_filter"] = from_none(self.geo_filter)
        result["children"] = from_list(lambda x: to_class(Child, x), self.children)
        result["before"] = from_none(self.before)
        return result


class RedditResponse:
    kind: str
    data: RedditResponseData

    def __init__(self, kind: str, data: RedditResponseData) -> None:
        self.kind = kind
        self.data = data

    @staticmethod
    def from_dict(obj: Any) -> 'RedditResponse':
        assert isinstance(obj, dict)
        kind = from_str(obj.get("kind"))
        data = RedditResponseData.from_dict(obj.get("data"))
        return RedditResponse(kind, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["kind"] = from_str(self.kind)
        result["data"] = to_class(RedditResponseData, self.data)
        return result


def reddit_response_from_dict(s: Any) -> RedditResponse:
    return RedditResponse.from_dict(s)


def reddit_response_to_dict(x: RedditResponse) -> Any:
    return to_class(RedditResponse, x)
