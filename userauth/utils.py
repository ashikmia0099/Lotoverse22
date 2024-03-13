import uuid
from django.conf import settings


def generate_ref_code():
    
    code = str(uuid.uuid4()).replace('-','')[: 12]

    return code


def generate_refferal_link(request):
    base_url = settings.BASE_URL
    
    if request.user.is_authenticated:
        
        try:
            user_sponsor = request.user.sponsor
            refferal_code = user_sponsor.code
            referral_link = f"{base_url}/userauth/metamask/?ref_code={refferal_code}"
            
            return referral_link
        except Sponsor.DoesNotExist:
            return f"{base_url}/userauth/metamask/"
    else:
        return f"{base_url}/userauth/metamask/"
