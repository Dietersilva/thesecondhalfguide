// Gate for the internal /SECONDSOCIAL dashboard and its API route.
// Fails closed: with no SECONDSOCIAL_PASSWORD set, these paths return 404.
export const config = { matcher: ['/secondsocial', '/secondsocial/:path*', '/api/secondsocial/:path*'] };

export default function middleware(request) {
  const headers = { 'X-Robots-Tag': 'noindex, nofollow', 'Cache-Control': 'no-store' };
  const pass = process.env.SECONDSOCIAL_PASSWORD;
  if (!pass) return new Response('Not found', { status: 404, headers });
  const auth = request.headers.get('authorization') || '';
  if (auth.startsWith('Basic ')) {
    let given = '';
    try { given = atob(auth.slice(6)).split(':').slice(1).join(':'); } catch (e) {}
    if (given.length === pass.length && given === pass) return; // continue to the file or route
  }
  return new Response('Authentication required', {
    status: 401,
    headers: { ...headers, 'WWW-Authenticate': 'Basic realm="SECONDSOCIAL", charset="UTF-8"' },
  });
}
